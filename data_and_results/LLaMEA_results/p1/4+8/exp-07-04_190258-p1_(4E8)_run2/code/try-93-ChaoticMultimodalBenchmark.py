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
        
        # Additional coupling term with increased complexity and modified interaction
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.15 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Introduce a new chaotic component with fractional exponents and additional trigonometric modulation
        fractional_chaos = 0
        for i in range(self.dim):
            fractional_chaos += np.sin(0.7 * x[i]**1.5) * np.cos(0.9 * x[i]**0.7) * np.exp(-0.03 * np.abs(x[i])) * np.log(1 + np.abs(x[i]))
        
        # Add a new multi-modal term with aperiodic chaotic behavior and enhanced interference
        aperiodic = 0
        for i in range(self.dim):
            aperiodic += np.sin(1.3 * x[i]) * np.cos(1.7 * x[i]) * np.tan(0.4 * x[i]) * np.exp(-0.04 * x[i]**2) * np.sin(0.2 * x[i]**4)
        
        # Combine all components with adjusted weights for better balance and increased multimodality
        return 0.8 * quadratic + 1.2 * chaotic + 0.9 * saddle + 1.1 * cross + 0.7 * interference + 1.0 * hyperbolic + 0.6 * high_order + 1.3 * log_perturbation + 0.8 * coupling + 1.5 * fractional_chaos + 1.4 * aperiodic