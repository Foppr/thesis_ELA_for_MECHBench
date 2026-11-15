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
        tent_map = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_map += 0.8 * x[i]
            else:
                tent_map += 0.8 * (1.0 - x[i])
        result += 1.5 * tent_map
        
        # Fractional polynomial distortions with non-integer exponents
        fractional_poly = 0.0
        for i in range(self.dim):
            fractional_poly += 0.7 * (x[i]**2.7 + 0.3 * x[i]**3.1 + 0.1 * x[i]**4.2)
        result += fractional_poly
        
        # Novel hyperbolic sine-cosine interaction terms
        hyperbolic_interaction = 0.0
        for i in range(self.dim - 1):
            hyperbolic_interaction += 1.2 * np.sinh(x[i]) * np.cosh(x[i+1]) + 0.9 * np.cosh(x[i]) * np.sinh(x[i+1])
        result += hyperbolic_interaction
        
        # Modified interdimensional coupling with hyperbolic tangent
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += 0.5 * np.tanh(x[i] * x[i+1]) * np.sin(x[i] + x[i+1])
        result += coupling
        
        # Additional multimodal peaks with modified Gaussian and hyperbolic combinations
        peaks = 0.0
        for i in range(self.dim):
            peaks += 0.8 * np.exp(-0.3 * (x[i]**2 - 1.5)**2) * np.cosh(3.0 * x[i])**2
        result += peaks
        
        # Enhanced chaotic perturbation with logistic map
        logistic = 0.0
        r = 3.95
        for i in range(self.dim):
            logistic += 0.4 * np.sin(r * x[i] * (1.0 - x[i]))
        result += logistic
        
        # Saddle point perturbations with modified trigonometric functions
        saddle = 0.0
        for i in range(self.dim):
            saddle += 0.2 * np.sin(0.8 * x[i]) * np.cos(0.5 * x[i]) * np.tanh(x[i]**2)
        result += saddle
        
        # Novel interaction term combining exponential and fractional components
        novel_interaction = 0.0
        for i in range(self.dim):
            novel_interaction += 0.3 * np.exp(-0.15 * np.abs(x[i])) * x[i]**3.5
        result += novel_interaction
        
        return result