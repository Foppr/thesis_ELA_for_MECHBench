import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies and exponential damping
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
        
        # Modified hyperbolic and logarithmic perturbations with added interdimensional coupling
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + np.abs(x[i])) * np.tanh(x[i]**2) * np.sin(0.3 * x[i]**4)
        
        # New logarithmic coupling term between dimensions to increase conditioning
        log_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                log_coupling += 0.05 * np.log(1 + np.abs(x[i] * x[j])) * np.cos(0.2 * (x[i]**2 + x[j]**2))
        
        # Additional higher-order polynomial and trigonometric coupling
        high_order = 0
        for i in range(self.dim):
            high_order += 0.05 * x[i]**6 * np.cos(0.2 * x[i]**3) * np.sin(0.1 * x[i])
        
        # New chaotic perturbation with modified exponential damping and enhanced trigonometric interference
        new_chaotic = 0
        for i in range(self.dim):
            new_chaotic += np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.tan(0.3 * x[i]) * np.exp(-0.03 * x[i]**2) * np.sin(0.2 * x[i]**4)
        
        # Increased trigonometric complexity with additional coupling terms
        trig_complexity = 0
        for i in range(self.dim):
            trig_complexity += 0.1 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.tan(0.4 * x[i]) * np.sin(0.15 * x[i]**5)
        
        # Enhanced interdimensional coupling with modified logarithmic terms
        enhanced_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                enhanced_coupling += 0.03 * np.log(1 + np.abs(x[i] * x[j])) * np.sin(0.25 * (x[i]**2 + x[j]**2)) * np.cos(0.1 * x[i] * x[j])
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + log_coupling + high_order + new_chaotic + trig_complexity + enhanced_coupling