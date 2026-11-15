import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies and modified exponential damping
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(11 * x[i]) * np.cos(7 * x[i]) * np.tan(0.7 * x[i]) * 
                       np.exp(-0.05 * x[i]**2) * np.sin(0.15 * x[i]**3))
        
        # Higher-order saddle point structure with quartic and quintic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**6 - 4 * x[i]**4 + 3 * x[i]**2) * np.cos(0.6 * x[i])
        
        # Complex cross-term interactions with higher-degree polynomials and trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * (x[i]**4 + x[j]**4) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic interference term with mixed trigonometric and polynomial components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                interference += 0.15 * np.sin(3 * x[i] + 4 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Hyperbolic and logarithmic perturbations to increase landscape complexity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + np.abs(x[i])) * np.tanh(x[i]**3) * np.sin(0.4 * x[i]**5)
        
        # Additional higher-order polynomial and trigonometric coupling with modified coefficient
        high_order = 0
        for i in range(self.dim):
            high_order += 0.08 * x[i]**7 * np.cos(0.25 * x[i]**4) * np.sin(0.15 * x[i])
        
        # New logarithmic perturbation with different base (base 10)
        log_perturbation = 0
        for i in range(self.dim):
            log_perturbation += np.log10(x[i]**2 + 1) * np.sin(0.25 * x[i])
        
        # Additional chaotic coupling term with exponential and trigonometric components
        chaotic_coupling = 0
        for i in range(self.dim):
            chaotic_coupling += np.exp(-0.02 * x[i]**2) * np.sin(0.3 * x[i]) * np.cos(0.1 * x[i]**3)
        
        # Cubic cross-term interactions with enhanced complexity
        cubic_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    cubic_cross += 0.1 * x[i] * x[j] * x[k] * np.sin(0.2 * (x[i]**3 + x[j]**3 + x[k]**3))
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + log_perturbation + chaotic_coupling + cubic_cross