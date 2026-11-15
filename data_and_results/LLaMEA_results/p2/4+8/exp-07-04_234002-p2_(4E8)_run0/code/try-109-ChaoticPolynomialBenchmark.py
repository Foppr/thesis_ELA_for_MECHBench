import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add exponential decay terms with polynomial components
        for i in range(self.dim):
            # Exponential decay with polynomial modulation
            exp_term = np.exp(-0.5 * x[i]**2) * (1.0 + 0.1 * x[i]**2 + 0.01 * x[i]**4)
            # Trigonometric modulation
            trig_term = np.sin(3.0 * x[i]) + 0.5 * np.cos(2.0 * x[i])
            # Asymmetric polynomial
            poly_term = 0.3 * x[i]**3 + 0.1 * x[i]**5
            result += exp_term * trig_term + poly_term
            
        # Cross-dimensional coupling with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                # Chaotic interaction term
                chaotic_interaction = np.sin(5.0 * x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                # Asymmetric coupling coefficient
                coupling = 0.2 * (1.0 + 0.3 * np.sin(x[i])) * (1.0 + 0.2 * np.cos(x[j]))
                result += coupling * chaotic_interaction
                
        # Add global conditioning with high-order polynomial terms
        sum_x2 = np.sum(x**2)
        sum_x4 = np.sum(x**4)
        sum_x6 = np.sum(x**6)
        
        # Global scaling factor with chaotic modulation
        global_factor = 1.0 + 0.5 * sum_x2 + 0.1 * sum_x4 + 0.02 * sum_x6
        # Add chaotic perturbation
        perturbation = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        result = result * global_factor + perturbation
        
        return result