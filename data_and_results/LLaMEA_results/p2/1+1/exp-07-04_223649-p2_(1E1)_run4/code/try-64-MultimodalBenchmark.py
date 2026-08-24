import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic tent map perturbations with varying parameter
        tent_perturbation = 0.0
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent_perturbation += 0.5 * xi
            else:
                tent_perturbation += 0.5 * (1.0 - xi)
        result += 1.5 * tent_perturbation
        
        # Fractional polynomial distortions with non-integer exponents
        fractional_poly = 0.8 * np.sum(np.abs(x)**1.7 + 0.3 * np.abs(x)**2.3 + 0.1 * np.abs(x)**3.1)
        
        # Radial basis function interactions with Gaussian and multiquadric kernels
        rbf_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                rbf_interaction += np.exp(-0.5 * diff**2) + 0.5 * np.sqrt(diff**2 + 0.1)
        result += 1.2 * rbf_interaction
        
        # Enhanced sine-cosine interaction with phase shifts and amplitude modulation
        sc_interaction = 0.0
        for i in range(self.dim):
            sc_interaction += np.sin(3.0 * x[i] + 0.5) * np.cos(2.0 * x[i] + 1.0) * np.sin(0.7 * x[i])
        result += 1.0 * sc_interaction
        
        # Modified hyperbolic and trigonometric coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += np.tanh(x[i]) * np.cos(x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        result += 0.9 * coupling
        
        # Novel multimodal peaks using asymmetric Gaussian and sinc combinations
        peaks = 0.0
        for i in range(self.dim):
            peaks += 0.7 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.sinc(x[i] - 1.0) + 0.3 * np.exp(-0.5 * (x[i] + 2.0)**2) * np.sinc(x[i] + 1.0)
        result += 1.3 * peaks
        
        # Additional chaotic perturbation using logistic map
        logistic_perturbation = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            logistic_perturbation += 0.4 * x[i] * (1.0 - x[i]) * r
        result += 0.8 * logistic_perturbation
        
        # Saddle point perturbations with modified hyperbolic functions
        saddle = 0.0
        for i in range(self.dim):
            saddle += 0.2 * np.sinh(0.5 * x[i]) * np.cos(0.3 * x[i]) * np.tanh(x[i]**2)
        result += 0.5 * saddle
        
        # Combine all terms
        result = result + fractional_poly + rbf_interaction + sc_interaction + coupling + peaks + logistic_perturbation + saddle
        
        return result