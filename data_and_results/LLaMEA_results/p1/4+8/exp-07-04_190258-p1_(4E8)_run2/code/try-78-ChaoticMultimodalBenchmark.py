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
            chaotic += (np.sin(9 * x[i]) * np.cos(5 * x[i]) * np.tan(0.5 * x[i]) * 
                       np.exp(-0.05 * x[i]**2) * np.sin(0.1 * x[i]**3))
        
        # Higher-order saddle point structure with quartic and quintic terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**5 - 3 * x[i]**3 + 2 * x[i]) * np.cos(0.5 * x[i])
        
        # Complex cross-term interactions with higher-degree polynomials and trigonometric coupling
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic interference term with mixed trigonometric and polynomial components
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity control
                interference += 0.1 * np.sin(2 * x[i] + 3 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Hyperbolic and logarithmic perturbations to increase landscape complexity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + np.abs(x[i])) * np.tanh(x[i]**2) * np.sin(0.3 * x[i]**4)
        
        # Additional higher-order polynomial and trigonometric coupling with modified coefficient
        high_order = 0
        for i in range(self.dim):
            high_order += 0.05 * x[i]**6 * np.cos(0.2 * x[i]**3) * np.sin(0.1 * x[i])
        
        # New logarithmic perturbation with different base (base 10) to increase discrimination
        log_perturbation = 0
        for i in range(self.dim):
            log_perturbation += np.log10(x[i]**2 + 1) * np.sin(0.2 * x[i])
        
        # Additional chaotic coupling term with modified frequency and amplitude
        chaotic_coupling = 0
        for i in range(self.dim):
            chaotic_coupling += 0.3 * np.sin(1.5 * x[i]) * np.cos(0.8 * x[i]) * np.exp(-0.02 * x[i]**2)
        
        # Modified exponential damping factor and increased trigonometric complexity
        trig_complexity = 0
        for i in range(self.dim):
            trig_complexity += 0.1 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.tan(0.3 * x[i]) * np.exp(-0.04 * x[i]**2)
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + log_perturbation + chaotic_coupling + trig_complexity