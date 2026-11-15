import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with exponential growth
        self.r_constants = np.exp(np.linspace(1.0, 3.0, dim))
        self.sigma = 0.05
        # Additional chaotic sequence for higher complexity
        self.chebyshev_coeffs = np.cos(np.linspace(0, np.pi, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic logistic map with Chebyshev polynomials
        logistic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            r = self.r_constants[i]
            x_i = x_norm[i]
            # Add Chebyshev modulation to logistic map
            cheb_mod = self.chebyshev_coeffs[i] * np.sin(x_i * np.pi)
            logistic_terms[i] = r * x_i * (1 - x_i) + 0.1 * cheb_mod
        
        # Multi-scale radial basis functions with varying centers
        rbfs = np.zeros(self.dim)
        for i in range(self.dim):
            # Dynamic centers based on dimension index
            center = np.sin(i * np.pi / (self.dim + 1)) * np.cos(i * np.pi / (self.dim + 2))
            # Add adaptive width parameter
            width = 0.5 + 0.5 * np.sin(i * np.pi / self.dim)
            rbfs[i] = (x_norm[i] - center)**2 + self.sigma * width
        
        # Enhanced gradient modulation with multiple frequencies
        grad_mod = np.zeros(self.dim)
        for i in range(self.dim):
            # Multiple frequency components
            freq1 = np.exp(-0.5 * (x_norm[i] / (i + 1.0))**2)
            freq2 = np.exp(-0.3 * (x_norm[i] / (i + 2.0))**2)
            freq3 = np.exp(-0.1 * (x_norm[i] / (i + 3.0))**2)
            grad_mod[i] = freq1 + 0.5 * freq2 + 0.3 * freq3
        
        # Additional nonlinear terms with higher-order interactions
        term1 = np.sum(logistic_terms**2)
        term2 = np.sum(1.0 / rbfs)
        term3 = np.sum(grad_mod * np.sin(7 * x_norm))
        term4 = np.sum(np.cos(5 * x_norm) * np.exp(-0.15 * x_norm**2))
        term5 = 0.3 * np.sum((x_norm[0] * x_norm[1])**6)
        
        # Novel cross-dimensional coupling with fractal-like behavior
        coupling = 0.0
        for i in range(self.dim - 1):
            # Fractal-like coupling with multiple scales
            scale1 = np.sin(x_norm[i] * x_norm[i+1])
            scale2 = np.cos(x_norm[i] * x_norm[i+1] * 2)
            scale3 = np.sin(x_norm[i] * x_norm[i+1] * 3)
            coupling += (x_norm[i] - x_norm[i+1])**2 * (scale1 + 0.5 * scale2 + 0.3 * scale3)
        
        # Add higher-order polynomial interactions
        poly_interaction = 0.0
        for i in range(0, self.dim - 2, 2):
            if i + 2 < self.dim:
                poly_interaction += (x_norm[i] * x_norm[i+1] * x_norm[i+2])**3
        
        # Add multi-modal sinusoidal component
        multi_modal = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Add noise with dynamic amplitude
        noise = 0.02 * np.random.random() * (1 + 0.5 * np.sin(np.sum(x_norm)))
        
        return term1 + term2 + term3 + term4 + term5 + coupling + poly_interaction + multi_modal + noise