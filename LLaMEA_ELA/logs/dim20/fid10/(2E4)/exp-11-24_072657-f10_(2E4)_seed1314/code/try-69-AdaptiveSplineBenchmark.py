import numpy as np

class AdaptiveSplineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spline control points for different dimensionalities
        np.random.seed(42)
        self.spline_points = np.random.uniform(-1, 1, (dim, 5))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Adaptive cubic spline interpolation with dimension-dependent control
        spline_result = 0.0
        for i in range(self.dim):
            # Use neighboring spline points for interpolation
            points = self.spline_points[i]
            # Cubic spline evaluation at x_norm[i]
            if len(points) >= 4:
                # Simple cubic interpolation using 4 control points
                t = (x_norm[i] + 1) / 2  # Normalize to [0,1]
                if t < 0: t = 0
                elif t > 1: t = 1
                # Cubic spline with boundary conditions
                p0, p1, p2, p3 = points[:4]
                spline_result += (2*t**3 - 3*t**2 + 1)*p0 + (-2*t**3 + 3*t**2)*p1 + (t**3 - 2*t**2 + t)*p2 + (t**3 - t**2)*p3
        
        # Logarithmic conditioning with varying exponents
        log_condition = np.sum(np.log(1 + np.abs(x_norm)) * (1 + 0.5 * np.sin(x_norm * np.pi)))
        
        # Cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1 + np.exp(-0.5 * (x_norm[i] + x_norm[i+1])))
            cross_coupling += weight * (x_norm[i] - x_norm[i+1])**2
        
        # Multi-scale oscillations with exponential decay
        oscillation = 0.0
        for i in range(self.dim):
            freqs = [2, 5, 8, 12]
            for f in freqs:
                oscillation += np.sin(f * x_norm[i]) * np.exp(-0.1 * f**2)
        
        # Adaptive conditioning based on dimensionality
        dim_cond = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combined function with varying contributions
        result = (0.4 * spline_result + 0.3 * log_condition + 0.2 * cross_coupling + 0.1 * oscillation) * dim_cond
        
        # Add small random perturbation for increased complexity
        noise = 0.0001 * np.random.random()
        
        return result + noise