import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term with asymmetric coefficients
        polynomial = 0.0
        for i in range(self.dim):
            polynomial += 0.1 * x[i]**2 + 0.05 * x[i]**3 + 0.01 * x[i]**4
        
        # Trigonometric oscillations with varying frequencies and phases
        trigonometric = 0.0
        for i in range(self.dim):
            trigonometric += np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            trigonometric += 0.5 * np.cos(4 * x[i]) * np.sin(5 * x[(i + 2) % self.dim])
            trigonometric += 0.3 * np.sin(6 * x[i]) * np.cos(3 * x[(i + 3) % self.dim])
        
        # Exponential interaction terms with asymmetric weights
        exponential = 0.0
        for i in range(self.dim):
            exponential += 0.2 * np.exp(-0.5 * (x[i] - 1)**2) * np.sin(2 * x[(i + 1) % self.dim])
            exponential += 0.15 * np.exp(-0.3 * (x[i] + 2)**2) * np.cos(3 * x[(i + 2) % self.dim])
            exponential += 0.1 * np.exp(-0.7 * (x[i] - 3)**2) * np.sin(4 * x[(i + 3) % self.dim])
        
        # Cross-dimensional interaction with non-linear coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            cross_interaction += 0.25 * (x[i] * x[(i + 1) % self.dim])**2
            cross_interaction += 0.1 * np.abs(x[i] - x[(i + 1) % self.dim]) * np.sin(3 * x[i])
            cross_interaction += 0.05 * x[i]**2 * x[(i + 2) % self.dim]**3
        
        # Asymmetric multimodal component with varying amplitude
        asymmetric = 0.0
        for i in range(self.dim):
            if i % 2 == 0:
                asymmetric += 0.3 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim])
            else:
                asymmetric += 0.4 * np.cos(6 * x[i]) * np.sin(3 * x[(i + 1) % self.dim])
        
        # Final fitness calculation with balanced weighting
        return 0.9 * polynomial + 1.2 * trigonometric + 1.5 * exponential + 1.0 * cross_interaction + 0.8 * asymmetric