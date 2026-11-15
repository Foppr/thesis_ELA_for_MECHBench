import numpy as np

class ChaoticRadialSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_params = np.random.uniform(3.5, 4.0, dim)
        self.radial_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.saddle_points = np.random.uniform(-4.0, 4.0, (dim, 2))
        self.time = 0.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic component using logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Time-varying chaotic parameter
            param = self.chaotic_params[i] * (1.0 + 0.1 * np.sin(self.time * 0.1 + i))
            # Logistic map iteration
            x_0 = 0.5
            for _ in range(100):
                x_0 = param * x_0 * (1.0 - x_0)
            chaotic += x_0 * (x[i] ** 2)
        
        # Radial basis function component with time-varying centers
        radial = 0.0
        for i in range(self.dim):
            center = self.radial_centers[i] + 0.5 * np.sin(self.time * 0.05 + i) * np.array([1.0, 0.5, 0.3])
            radial += np.exp(-0.5 * np.sum(((x[i] - center) / (1.0 + 0.1 * i)) ** 2))
        
        # Saddle-point structure with time-varying saddle points
        saddle = 0.0
        for i in range(self.dim):
            saddle_point = self.saddle_points[i] + 0.3 * np.cos(self.time * 0.03 + i)
            saddle += (x[i] - saddle_point[0]) ** 2 - (x[i] - saddle_point[1]) ** 2
        
        # Cross-dimensional coupling with interaction matrix
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength
                coupling = 0.5 + 0.3 * np.sin(self.time * 0.02 + i + j)
                cross += coupling * np.sin(x[i] * x[j]) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Polynomial and trigonometric mixture with dynamic exponents
        poly_trig = 0.0
        for i in range(self.dim):
            # Dynamic exponent based on time and dimension
            exp_val = 2.0 + 0.5 * np.sin(self.time * 0.04 + i)
            poly_trig += (x[i] ** exp_val) * np.cos(x[i] * 0.5)
        
        # Global scaling and time-dependent modulation
        self.time += 0.01
        scale_factor = 1.0 + 0.2 * np.sin(self.time * 0.05)
        
        # Combine all components
        result = scale_factor * (chaotic + radial + saddle + cross + poly_trig)
        return result