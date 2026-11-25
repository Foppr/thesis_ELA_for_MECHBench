import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic component with fractal-like structure
        chaotic = 0.0
        r = 3.95
        for i in range(self.dim):
            x_prev = 0.5
            for _ in range(20):  # More iterations for deeper chaos
                x_prev = r * x_prev * (1 - x_prev)
            chaotic += np.sin(x_normalized[i] * x_prev * 15) * np.cos(x_normalized[i] * x_prev * 10) * np.exp(-np.abs(x_normalized[i]))
        
        # Enhanced gradient with adaptive conditioning
        gradient = 0.0
        for i in range(self.dim):
            condition = 1.0 + 4.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            gradient += condition * (x_normalized[i] ** 4) * np.exp(-0.2 * x_normalized[i]**2)
        
        # Enhanced saddle point region with multi-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                saddle += np.tanh(x_normalized[i]) * np.tanh(x_normalized[j]) * (x_normalized[i] - x_normalized[j])**3
        
        # Multi-modal discontinuous region with fractal step function
        discontinuous = 0.0
        for i in range(self.dim):
            step_val = 1.0 if x_normalized[i] > 0 else -1.0
            discontinuous += step_val * np.sin(8 * x_normalized[i]) * np.cos(6 * x_normalized[i]) * (1 + 0.5 * np.sin(3 * x_normalized[i]))
        
        # Enhanced harmonic interaction with fractal scaling
        harmonic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = np.exp(-dist * 5.0) * (1 + 0.3 * np.sin(dist * 10))
                harmonic += weight * np.sin(4 * (x_normalized[i] + x_normalized[j])) * np.cos(4 * (x_normalized[i] - x_normalized[j]))
        
        # Multi-scale nonlinearity with fractal component
        nonlin = 0.0
        for i in range(self.dim):
            nonlin += (x_normalized[i]**5) * np.sin(x_normalized[i])**3 * np.exp(-np.abs(x_normalized[i]))
        
        # Additional multi-modal component with Gaussian mixture
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.exp(-0.5 * (x_normalized[i] - 1.5)**2) + np.exp(-0.5 * (x_normalized[i] + 1.5)**2) - 1.0
        
        # Combined fitness with dynamic scaling
        return (0.25 * chaotic + 0.2 * gradient + 0.18 * saddle + 
                0.18 * discontinuous + 0.12 * harmonic + 0.07 * nonlin + 0.05 * multimodal)