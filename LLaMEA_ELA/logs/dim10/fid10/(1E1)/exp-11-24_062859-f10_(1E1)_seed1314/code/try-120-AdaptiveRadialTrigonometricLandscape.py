import numpy as np

class AdaptiveRadialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive conditioning
        result = 0.1 * np.sum(x**2)
        
        # Radial basis function components with varying widths
        for i in range(self.dim):
            # Gaussian RBF with position-dependent width
            width = 1.0 + 0.5 * np.sin(0.5 * x[i])
            result += 3.0 * np.exp(-0.5 * (x[i] / width)**2)
        
        # Multi-scale trigonometric interference
        for i in range(self.dim):
            result += 2.5 * np.sin(3 * x[i]) * np.cos(7 * x[i])
            
        # Asymmetric polynomial terms with cross-dimensional coupling
        for i in range(self.dim):
            if x[i] >= 0:
                result += 1.2 * x[i]**4
            else:
                result += 0.8 * x[i]**6
                
        # Cross-dimensional interaction with variable coupling strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.5 + 0.3 * np.sin(0.3 * (x[i] + x[j]))
                result += coupling * np.sin(2 * x[i]) * np.cos(3 * x[j])
        
        # Adaptive conditioning based on coordinate values
        for i in range(self.dim):
            condition_factor = 1.0 + 0.8 * np.abs(x[i]) / 5.0
            result += 0.5 * condition_factor * x[i]**2
        
        # High-frequency oscillation with amplitude modulation
        for i in range(self.dim):
            result += 1.8 * np.sin(15 * x[i]) * np.cos(9 * x[i]) * (1 + 0.3 * np.tanh(x[i]))
        
        # Add noise to prevent trivial solutions
        result += 0.02 * np.random.random()
        
        return result