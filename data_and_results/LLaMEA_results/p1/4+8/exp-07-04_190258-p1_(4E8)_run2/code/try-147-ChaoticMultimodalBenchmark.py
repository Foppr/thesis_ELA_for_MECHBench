import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with logarithmic modulation
        rbfs = 0
        for i in range(self.dim):
            rbfs += np.log(1 + 0.1 * (x[i] - 2)**2) * np.sin(4 * x[i]) + \
                   np.log(1 + 0.1 * (x[i] + 2)**2) * np.cos(3 * x[i])
        
        # Asymmetric saddle point structure with cubic modulation
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**3 - 3 * x[i]**2 + 2 * x[i]) * np.sin(0.7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with hyperbolic interactions
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * np.tanh(x[i] * x[j]) * np.sin(0.5 * (x[i]**2 + x[j]**2)) * \
                           np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Enhanced periodic interference with chaotic frequency modulation
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(6 * x[i]) * np.cos(5 * x[i]) * np.tan(0.3 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Modified exponential damping with asymmetric decay
        damping = 0
        for i in range(self.dim):
            damping += np.exp(-0.3 * np.abs(x[i])) * np.sin(0.2 * x[i]**3) * np.cos(0.1 * x[i])
        
        # Hyperbolic tangent modulation with polynomial enhancement
        tanh_mod = 0
        for i in range(self.dim):
            tanh_mod += np.tanh(x[i]) * np.cos(0.4 * x[i]**2) * np.exp(-0.02 * x[i]**2)
        
        # Quadratic base with enhanced sinusoidal perturbation and chaotic noise
        base = np.sum(x**2) + 0.2 * np.sum(np.sin(3 * x)**2) + 0.05 * np.sum(np.random.randn(self.dim) * x)
        
        # Additional chaotic modulation with fractional Brownian motion-like behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.tanh(0.2 * x[i]**3) * \
                      np.exp(-0.04 * x[i]**2) * np.sin(0.1 * np.sum(x**2))
        
        # Add a new component with Gaussian mixture model characteristics
        gaussian_mixture = 0
        for i in range(self.dim):
            gaussian_mixture += np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(2 * x[i]) + \
                               np.exp(-0.5 * (x[i] + 1.5)**2) * np.cos(2 * x[i])
        
        # Add a fractal-like component with recursive self-similarity
        fractal = 0
        for i in range(self.dim):
            fractal += np.sin(8 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.06 * x[i]**2) * \
                      np.sin(0.05 * np.sum(np.abs(x)))
        
        # Introduce a new chaotic component with fractional Brownian motion characteristics
        fbm_like = 0
        for i in range(self.dim):
            fbm_like += np.sin(9 * x[i]) * np.cos(7 * x[i]) * np.tanh(0.15 * x[i]**2) * \
                       np.exp(-0.07 * x[i]**2) * np.cos(0.08 * np.sum(x**2))
        
        # Add a new multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.03 * x[i]**2) + \
                         np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.04 * x[i]**2)
        
        # Combine all components with modified weights for better balance
        return 0.8 * base + 0.6 * rbfs + 0.5 * saddles + 0.7 * coupling + 0.4 * periodic + \
               0.6 * damping + 0.5 * tanh_mod + 0.7 * chaotic + 0.5 * gaussian_mixture + \
               0.6 * fractal + 0.3 * fbm_like + 0.4 * multimodal