import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic tent map perturbations with varying control parameters
        tent_map = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_map += 2.0 * x[i]
            else:
                tent_map += 2.0 * (1.0 - x[i])
        result += 1.5 * tent_map
        
        # Asymmetric cubic coupling with directional bias
        cubic_coupling = 0.0
        for i in range(self.dim - 1):
            cubic_coupling += (x[i] ** 3) * np.sin(x[i+1]) + (x[i+1] ** 3) * np.cos(x[i])
        result += 0.8 * cubic_coupling
        
        # Novel hyperbolic sine-cosine interaction terms
        hyperbolic_interaction = 0.0
        for i in range(self.dim):
            hyperbolic_interaction += np.sinh(x[i]) * np.cos(x[i]**2) + np.cosh(x[i]) * np.sin(x[i]**2)
        result += 1.2 * hyperbolic_interaction
        
        # Modified polynomial distortions with negative coefficients
        poly_distortion = -0.7 * np.sum(x**3 + 0.3 * x**5 - 0.1 * x**7 + 0.08 * x**9)
        result += poly_distortion
        
        # Logarithmic interdimensional coupling with exponential decay
        coupling = 0.5 * np.sum(np.log(1.0 + 0.3 * (x[:-1] - x[1:])**2) * np.exp(-0.2 * (x[:-1] + x[1:])**2))
        result += coupling
        
        # Additional multimodal peaks with modified Gaussian and hyperbolic combinations
        peaks = 0.8 * np.sum(np.exp(-0.3 * (x**2 - 1.5)**2) * np.tanh(2.0 * x)**2)
        result += peaks
        
        # Enhanced chaotic perturbation with logistic map dynamics
        logistic_perturbation = 0.0
        r = 3.95
        for i in range(self.dim):
            logistic_perturbation += np.sin(r * x[i] * (1.0 - x[i]))
        result += 0.4 * logistic_perturbation
        
        # Saddle point perturbations with modified trigonometric functions and exponential decay
        saddle = 0.2 * np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) * np.exp(-0.1 * x**2))
        result += saddle
        
        # Novel interaction term combining hyperbolic and polynomial components with chaotic modulation
        novel_interaction = 0.3 * np.sum(np.sinh(0.1 * x) * x**5 * np.cos(x))
        result += novel_interaction
        
        return result