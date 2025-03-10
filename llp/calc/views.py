from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64

import pulp

def graphical_method(request):
    if request.method == 'POST':
        try:
            # Get inputs from the form
            objective = request.POST.get('objective')  # 'maximize' or 'minimize'
            x_profit = float(request.POST.get('x_profit'))
            y_profit = float(request.POST.get('y_profit'))
            land_constraint = float(request.POST.get('land_constraint'))
            water_constraint = float(request.POST.get('water_constraint'))
            x_land = float(request.POST.get('x_land'))
            y_land = float(request.POST.get('y_land'))
            x_water = float(request.POST.get('x_water'))
            y_water = float(request.POST.get('y_water'))

            # Create the linear programming problem
            problem = pulp.LpProblem("CropOptimization", pulp.LpMaximize if objective == 'maximize' else pulp.LpMinimize)

            # Define decision variables
            x = pulp.LpVariable("x", lowBound=0)
            y = pulp.LpVariable("y", lowBound=0)

            # Define objective function
            problem += x_profit * x + y_profit * y, "TotalProfit"

            # Define constraints
            problem += x_land * x + y_land * y <= land_constraint, "LandConstraint"
            problem += x_water * x + y_water * y <= water_constraint, "WaterConstraint"

            # Solve the problem
            problem.solve()

            # Get the results
            x_optimal = pulp.value(x)
            y_optimal = pulp.value(y)
            optimal_value = pulp.value(problem.objective)

            return render(request, 'calc/graphical_method.html', {
                'x_optimal': x_optimal,
                'y_optimal': y_optimal,
                'optimal_value': optimal_value,
                'objective': objective,
                'land_constraint': land_constraint,
                'water_constraint': water_constraint,
                'x_land': x_land,
                'y_land': y_land,
                'x_water': x_water,
                'y_water': y_water
            })

        except ValueError:
            return render(request, 'calc/graphical_method.html', {'error': 'Invalid input. Please enter numeric values.'})

    return render(request, 'calc/graphical_method.html')


def home(request):
    return render(request, 'calc/home.html')

def optimization(request):
<<<<<<< HEAD
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
=======
    return render(request, 'calc/optimization.html')


def simplex_method(request):
    return render(request, 'calc/simplex_method.html')

def transportation_method(request):
    return render(request, 'calc/transportation_method.html')

def knapsack_method(request):
    return render(request, 'calc/knapsack_method.html')
>>>>>>> 3ebd374 (Updated optimization features and added missing templates)
