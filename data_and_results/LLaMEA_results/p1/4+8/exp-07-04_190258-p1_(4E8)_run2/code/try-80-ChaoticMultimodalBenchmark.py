import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Chaotic sine wave perturbations with varying frequencies and damping
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Polynomial saddle point structure with mixed powers
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 6 * x[i]**2 + 4) * np.sin(0.5 * x[i])
        
        # Cross-dimensional interactions with trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) * (x[i]**2 + x[j]**2)
        
        # Logarithmic coupling between dimensions with base e
        log_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                log_coupling += 0.2 * np.log(1 + np.abs(x[i] * x[j])) * np.sin(0.2 * (x[i] + x[j]))
        
        # Hyperbolic tangent perturbations to create sharp fitness changes
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.tanh(x[i]**3) * np.cos(0.3 * x[i]**2)
        
        # High-order polynomial terms with chaotic modulation
        high_order = 0
        for i in range(self.dim):
            high_order += 0.1 * x[i]**5 * np.sin(0.1 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Additional chaotic interference with exponential decay
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                interference += 0.15 * np.sin(2 * x[i] + x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Combined logarithmic and polynomial coupling
        combined = 0
        for i in range(self.dim):
            combined += 0.25 * np.log(1 + x[i]**2) * x[i] * np.cos(0.4 * x[i])
        
        return quadratic + chaotic + saddle + cross + log_coupling + hyperbolic + high_order + interference + combined