import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with multiple frequencies, exponential damping, and irrational multipliers
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(np.pi * 9 * x[i]) * np.cos(np.e * 5 * x[i]) * np.tan(0.5 * x[i]) * 
                       np.exp(-0.05 * x[i]**2) * np.sin(0.1 * x[i]**3) * np.cos(np.sqrt(2) * x[i]))
        
        # Higher-order saddle point structure with quartic and quintic terms and irrational coupling
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**5 - 3 * x[i]**3 + 2 * x[i]) * np.cos(0.5 * x[i]) * np.sin(np.sqrt(3) * x[i])
        
        # Complex cross-term interactions with higher-degree polynomials, trigonometric coupling, and irrational constants
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += 0.2 * x[i] * x[j] * (x[i]**3 + x[j]**3) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.sin(np.phi * x[i] * x[j])
        
        # Additional chaotic interference term with mixed trigonometric and polynomial components, irrational coupling
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity control
                interference += 0.1 * np.sin(2 * x[i] + 3 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2) * np.cos(np.sqrt(5) * x[i])
        
        # Hyperbolic and logarithmic perturbations with irrational bases and enhanced complexity
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.log(1 + np.abs(x[i])) * np.tanh(x[i]**2) * np.sin(0.3 * x[i]**4) * np.cos(np.pi * x[i])
        
        # Additional higher-order polynomial and trigonometric coupling with irrational multipliers
        high_order = 0
        for i in range(self.dim):
            high_order += 0.05 * x[i]**6 * np.cos(0.2 * x[i]**3) * np.sin(0.1 * x[i]) * np.tan(np.e * x[i])
        
        # Add irrational constant for global scaling
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + np.pi