import numpy as np

class ChaoticRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with varying conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add chaotic radial basis functions with dynamic centers
        rb_sum = 0
        centers = np.linspace(-4.0, 4.0, min(15, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i % len(centers)]
            # Dynamic scaling based on dimension
            scale = 1.0 + 0.5 * np.sin(i * 0.5)
            rb_sum += scale * np.exp(-0.5 * ((x[i % self.dim] - center) / (1.0 + 0.1 * i))**2)
        f += 2.0 * rb_sum
        
        # Add gradient field interactions with time-like parameter
        grad_field = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dynamic interaction based on position and dimension
                interaction = np.sin(3 * (x[i] + x[j])) * np.cos(2 * (x[i] - x[j]))
                grad_field += interaction * (1.0 + 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4))
        f += 1.5 * grad_field
        
        # Add chaotic phase modulation with nested structure
        phase = 0
        for i in range(self.dim):
            phase += np.sin(2 * np.pi * x[i] * (i + 1) * 0.2) * np.cos(np.pi * x[i] * (i + 1) * 0.15)
        f += 0.8 * np.sin(phase)
        
        # Add multi-scale sinusoidal modulations
        mod_sum = 0
        for i in range(self.dim):
            mod_sum += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(5 * x[i])
        f += 1.2 * mod_sum
        
        # Add chaotic coupling terms with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        f += 0.6 * coupling
        
        # Add fractal-like self-similarity with recursive pattern
        fractal = 0
        for i in range(self.dim):
            fractal += np.sin(8 * np.sin(3 * x[i])) * np.cos(5 * np.cos(2 * x[i]))
        f += 0.4 * fractal
        
        # Add non-linear transformation with dynamic parameters
        nonlinear = 0
        for i in range(self.dim):
            nonlinear += (x[i]**3) * np.sin(x[i]) * np.cos(0.5 * x[i])
        f += 0.3 * nonlinear
        
        # Add dynamic noise component
        noise = 0
        for i in range(self.dim):
            noise += np.sin(15 * x[i]) * np.cos(12 * x[i]) * np.sin(9 * x[i])
        f += 0.1 * noise
        
        return f