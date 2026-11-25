import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize time-varying parameters for chaotic dynamics
        self.t = 0.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        self.t += 0.01
        
        # Time-varying chaotic component with saddle-point characteristics
        chaotic = 0.0
        for i in range(self.dim):
            t_var = np.sin(self.t + i * 0.7) * np.cos(self.t * 0.5 + i * 0.3)
            chaotic += (x[i]**2 - 1.0)**2 * t_var
        
        # Fractal-like basin boundaries with multi-resolution interference
        fractal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * self.t + i)
            scale = 1.0 + 0.3 * np.cos(0.6 * self.t + i)
            fractal += scale * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8) * np.exp(-0.1 * x[i]**2)
        
        # Multi-resolution harmonic interference with dynamic phase coupling
        interference = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.3 * self.t + i * 0.9) + 0.2 * np.cos(0.7 * self.t + i * 0.4)
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.5 + 0.5 * np.sin(0.2 * (i + j) + self.t)
                dist = np.abs(x[i] - x[j])
                interference += coupling * np.sin(dist * 3.0 + phase) * np.exp(-dist * 0.3)
        
        # Dynamic gradient field with time-varying conditioning
        grad_field = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.4 * np.sin(0.5 * self.t + i * 0.6)
            grad_field += cond_factor * x[i]**3 * np.cos(x[i] * 0.5) * np.exp(-0.05 * x[i]**2)
        
        # Additional higher-order polynomial terms for complexity
        poly_terms = 0.0
        for i in range(self.dim):
            poly_terms += 0.1 * x[i]**8 + 0.05 * x[i]**9
        
        # Combined function with adaptive weights based on time
        weight1 = 0.3 + 0.1 * np.sin(0.2 * self.t)
        weight2 = 0.25 + 0.1 * np.cos(0.3 * self.t)
        weight3 = 0.2 + 0.05 * np.sin(0.4 * self.t)
        weight4 = 0.15 + 0.05 * np.cos(0.5 * self.t)
        weight5 = 0.1
        
        result = weight1 * chaotic + weight2 * fractal + weight3 * interference + weight4 * grad_field + weight5 * poly_terms
        
        # Dimension-dependent scaling with chaotic modulation
        dim_scale = 1.0 + 0.1 * np.sin(self.t * 0.8) + 0.05 * np.log(self.dim + 1)
        
        return result * dim_scale