import numpy as np

class AdaptiveValleyLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = 0.1 * np.sum(x**2)
        
        # Add multiple polynomial components with varying degrees and coefficients
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2.0 * x[i]**3 + 1.5 * x[i]**2
            
        # Add trigonometric components with adaptive frequencies based on dimension
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.5)
            result += 0.8 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * \
                     np.exp(-0.1 * np.abs(x[i]))
            
        # Add radial basis function components with adaptive centers and widths
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            result += 0.3 * np.exp(-0.5 * ((x - centers[i]) / (1.0 + 0.1 * i))**2)
            
        # Add asymmetric valley structure with different scaling factors
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.4 * (x[i] - 1)**3 * np.exp(-0.2 * x[i])
            else:
                result += 0.4 * (x[i] + 1)**3 * np.exp(-0.2 * np.abs(x[i]))
                
        # Add cross-dimensional coupling with asymmetric interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i % 2 == 0:
                    result += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                else:
                    result += 0.2 * np.cos(x[i]) * np.sin(x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    
        # Add a highly multimodal component with multiple local minima
        for i in range(self.dim):
            result += 0.6 * np.sin(3 * x[i]) + 0.4 * np.cos(5 * x[i]) + \
                     0.3 * np.sin(7 * x[i]) * np.cos(2 * x[i])
            
        # Add noise to prevent trivial solutions
        result += 0.01 * np.random.random()
        
        return result