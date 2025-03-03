from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64

def home(request):
    return render(request, 'calc/home.html')

def optimization(request):
    if request.method == "POST":
        # Get Farm Constraints
        total_land = float(request.POST["total_land"])
        total_budget = float(request.POST["total_budget"])
        total_water = float(request.POST["total_water"])
        total_labor = float(request.POST["total_labor"])
        total_fertilizer = float(request.POST["total_fertilizer"])
        optimization_goal = request.POST["optimization_goal"]

        # Get Crop Data
        crops = []
        for i in range(len(request.POST.getlist("crop_name"))):
            crops.append({
                "name": request.POST.getlist("crop_name")[i],
                "profit": float(request.POST.getlist("profit_per_acre")[i]),
                "land": float(request.POST.getlist("land_requirement")[i]),
                "water": float(request.POST.getlist("water_requirement")[i]),
                "labor": float(request.POST.getlist("labor_requirement")[i]),
                "fertilizer": float(request.POST.getlist("fertilizer_requirement")[i]),
                "growing_time": float(request.POST.getlist("growing_time")[i]),
            })

        # Knapsack-like Optimization
        selected_crops, total_profit, total_water_used, total_labor_used = knapsack_optimization(
            crops, total_land, total_water, total_labor
        )

        # Generate Charts
        crop_names = [crop["name"] for crop in selected_crops]
        land_allocations = [crop["land"] for crop in selected_crops]

        pie_chart = generate_pie_chart(crop_names, land_allocations)

        return render(request, "calc/optimization.html", {
            "selected_crops": selected_crops,
            "total_profit": total_profit,
            "total_water_used": total_water_used,
            "total_labor_used": total_labor_used,
            "pie_chart": pie_chart,
        })

    return render(request, "calc/optimization.html")

def knapsack_optimization(crops, total_land, total_water, total_labor):
    crops = sorted(crops, key=lambda x: x["profit"] / x["land"], reverse=True)

    selected_crops = []
    total_profit = 0
    total_water_used = 0
    total_labor_used = 0
    remaining_land = total_land

    for crop in crops:
        if crop["land"] <= remaining_land:
            selected_crops.append(crop)
            total_profit += crop["profit"]
            total_water_used += crop["water"]
            total_labor_used += crop["labor"]
            remaining_land -= crop["land"]

    return selected_crops, total_profit, total_water_used, total_labor_used

def generate_pie_chart(labels, sizes):
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.axis("equal")

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    string = base64.b64encode(buffer.read()).decode()
    buffer.close()
    return f"data:image/png;base64,{string}"