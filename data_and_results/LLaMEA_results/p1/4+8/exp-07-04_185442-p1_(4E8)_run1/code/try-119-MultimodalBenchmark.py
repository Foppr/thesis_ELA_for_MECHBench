import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with exponential growth
        self.r_constants = np.exp(np.linspace(1.0, 3.0, dim))
        self.sigma = 0.05
        self.alpha = np.linspace(0.5, 2.0, dim)
        self.beta = np.linspace(1.0, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map with time-varying parameters
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            # Add memory effect with previous value
            if i > 0:
                logistic_terms[i] = r * x_i * (1 - x_i) + 0.1 * np.sin(x_norm[i-1])
            else:
                logistic_terms[i] = r * x_i * (1 - x_i)
        
        # Multi-scale radial basis functions with varying widths
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            center = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            width = self.sigma * (1 + 0.5 * np.sin(i))
            rbfs[i] = (x_norm[i] - center)**2 + width
        
        # Adaptive gradient modulation with frequency modulation
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * np.cos(i * np.pi / self.dim)
            grad_mod[i] = np.exp(-0.5 * (x_norm[i] / (i + 1.0))**2) * np.sin(freq)
        
        # Enhanced sinusoidal interactions with polynomial coupling
        term1 = np.sum(logistic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(3 * x_norm))
        term4 = np.sum(np.cos(2 * x_norm) * np.exp(-0.1 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**6)
        
        # Multi-scale cross-dimensional coupling
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] - x_norm[i+1])**2 * np.sin(x_norm[i] * x_norm[i+1] * (i + 1))
        
        # Add higher-order polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim - 2):
            poly_interaction += (x_norm[i] * x_norm[i+1] * x_norm[i+2])**3
        
        # Add fractal-like self-similarity
        fractal = 0.0
        for i in range(1, self.dim):
            if i % 2 == 0:
                fractal += np.sin(x_norm[i] * 10) * np.cos(x_norm[i-1] * 5)
            else:
                fractal += np.cos(x_norm[i] * 8) * np.sin(x_norm[i-1] * 3)
        
        # Add noise with dynamic amplitude
        noise_amp = 0.02 * (1 + 0.5 * np.sin(np.sum(x_norm)))
        noise = noise_amp * np.random.random()
        
        return term1 + term2 + term3 + term4 + term5 + coupling + poly_interaction + fractal + noise