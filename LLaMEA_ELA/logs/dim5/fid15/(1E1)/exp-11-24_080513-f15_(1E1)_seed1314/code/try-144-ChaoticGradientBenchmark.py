import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with fractal-like behavior
        chaotic = 0.0
        r = 3.99
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10) * np.exp(-np.abs(x_normalized[i]))
        
        # Exponentially varying conditioning with global optima
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 5.0 * np.exp(-0.5 * (i - self.dim/2)**2)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with multiple coupling levels
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # More extensive coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Fractal-like discontinuity with multiple scales
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i]) * np.exp(-np.abs(x_normalized[i]))
        
        # Multi-scale harmonic with cross-dimensional interference
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 6.0)
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(5 * (x_normalized[i] - x_normalized[j]))
        
        # Additional nonlinearity with global optima alignment
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3
        
        # Add a global optimum attractor term
        optimum_attractor = 0.0
        center = np.ones(self.dim) * 0.1
        dist_from_center = np.linalg.norm(x_normalized - center)
        optimum_attractor = 2.0 * np.exp(-dist_from_center**2)
        
        # Combined fitness with modified scaling and added complexity
        return (0.25 * chaotic + 0.3 * gradient + 0.18 * saddle + 
                0.17 * discontinuous + 0.08 * harmonic + 0.02 * nonlin + 0.0 * optimum_attractor)