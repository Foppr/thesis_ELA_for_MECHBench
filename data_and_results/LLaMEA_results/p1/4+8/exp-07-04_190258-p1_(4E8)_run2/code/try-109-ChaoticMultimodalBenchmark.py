import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies, modified exponential damping, and hyperbolic terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(11 * x[i]) * np.cos(7 * x[i]) * np.tan(0.7 * x[i]) * 
                       np.exp(-0.08 * x[i]**2) * np.sin(0.15 * x[i]**3) * 
                       np.cosh(0.2 * x[i]) * np.log(1 + np.abs(x[i])))
        
        # Higher-order saddle point structure with quartic, quintic, and septic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**7 - 4 * x[i]**5 + 3 * x[i]**3 - x[i]) * np.cos(0.6 * x[i])
        
        # Complex cross-term interactions with higher-degree polynomials, trigonometric coupling, and exponential decay
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.3 * x[i] * x[j] * (x[i]**4 + x[j]**4) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Additional chaotic interference term with mixed trigonometric and polynomial components, increased complexity
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                interference += 0.15 * np.sin(3 * x[i] + 4 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2) * np.tanh(0.3 * x[i])
        
        # Hyperbolic and logarithmic perturbations with multiple bases to increase landscape complexity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + np.abs(x[i])) * np.tanh(x[i]**2) * np.sin(0.4 * x[i]**4) + np.log2(1 + x[i]**2) * np.cos(0.3 * x[i]**3)
        
        # Additional higher-order polynomial and trigonometric coupling with modified coefficient and chaotic modulation
        high_order = 0
        for i in range(self.dim):
            high_order += 0.08 * x[i]**7 * np.cos(0.25 * x[i]**3) * np.sin(0.12 * x[i]) * np.tan(0.1 * x[i])
        
        # New logarithmic perturbation with different base (base 10) and additional trigonometric modulation
        log_perturbation = 0
        for i in range(self.dim):
            log_perturbation += np.log10(x[i]**2 + 1) * np.sin(0.25 * x[i]) * np.cos(0.1 * x[i]**2)
        
        # Additional coupling term with increased complexity, modified interaction, and chaotic modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.2 * np.sin(0.4 * x[i]) * np.cos(0.5 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.03 * (x[i] - x[j])**2) * np.sin(0.2 * x[i]**3)
        
        # Additional chaotic modulation with fractal-like behavior
        fractal = 0
        for i in range(self.dim):
            fractal += 0.05 * np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.tan(0.8 * x[i]) * np.exp(-0.1 * x[i]**2) * np.sin(0.2 * x[i]**4)
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + log_perturbation + coupling + fractal