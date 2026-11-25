import numpy as np

class NeuralFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal and neural-inspired parameters
        self.fractal_exponents = np.random.rand(dim) * 0.8 + 0.2
        self.neural_weights = np.random.randn(dim) * 0.5 + 1.0
        self.saddle_points = np.random.randn(dim, 3) * 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal-like curvature variation with multi-scale oscillations
            fractal_curvature = 0.0
            for k in range(1, min(30, self.dim + 10)):
                fractal_curvature += (1.0 / (k**self.fractal_exponents[i])) * \
                                   np.sin(k * xi * (1.0 + 0.3 * np.cos(k * 0.5)))
            
            # Saddle-point potential with multiple stable and unstable directions
            saddle_potential = 0.0
            for j in range(len(self.saddle_points)):
                point = self.saddle_points[j]
                dist = np.sqrt((xi - point[0])**2 + (xi - point[1])**2 + (xi - point[2])**2)
                saddle_potential += point[0] * np.exp(-dist**2 / (2.0 * point[1]**2)) * \
                                  np.cos(point[2] * xi)
            
            # Neural-inspired activation-like modulation with non-linear response
            neural_modulation = np.tanh(xi * self.neural_weights[i]) * \
                               (1.0 + 0.3 * np.sin(xi * self.neural_weights[i] * 2.0))
            
            # Multi-scale interference pattern from neighboring dimensions
            interference = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    dist = np.abs(xi - x_norm[j])
                    interference += (1.0 / (1.0 + dist**2)) * \
                                  np.sin(xi * x_norm[j] * (1.0 + 0.2 * np.sin(i + j)))
            
            # Combine all terms with adaptive scaling
            term = (fractal_curvature + saddle_potential + neural_modulation + 0.5 * interference)**2
            result += term
            
        # Add global fractal scaling and noise modulation
        global_scaling = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.14) + \
                        0.1 * np.cos(np.log(self.dim + 1) * 2.0)
        
        return global_scaling * result / self.dim