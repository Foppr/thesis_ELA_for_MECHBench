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
        
        # Additional chaotic modulation with enhanced nonlinearity and increased interference
        chaotic_mod = 0
        for i in range(self.dim):
            chaotic_mod += 0.3 * np.sin(7 * x[i]) * np.cos(3 * x[i]) * np.tan(0.7 * x[i]) * np.exp(-0.03 * x[i]**2) * np.sin(0.15 * x[i]**4)
        
        # Increased trigonometric interference with more complex interaction
        trig_interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                trig_interference += 0.25 * np.sin(1.5 * x[i] + 2 * x[j]) * np.cos(0.8 * x[i] - 1.2 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Enhanced hyperbolic coupling with additional terms
        hyperbolic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hyperbolic_coupling += 0.1 * np.log(1 + np.abs(x[i])) * np.log(1 + np.abs(x[j])) * np.tanh(x[i]**2) * np.tanh(x[j]**2) * np.sin(0.2 * (x[i]**2 + x[j]**2))
        
        # Additional chaotic component with higher frequency and stronger coupling
        chaotic_high_freq = 0
        for i in range(self.dim):
            chaotic_high_freq += 0.4 * np.sin(12 * x[i]) * np.cos(8 * x[i]) * np.tan(0.9 * x[i]) * np.exp(-0.08 * x[i]**2) * np.sin(0.2 * x[i]**5)
        
        # Increased cross-term complexity with higher-order interactions
        cross_high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    cross_high_order += 0.05 * x[i] * x[j] * x[k] * (x[i]**2 + x[j]**2 + x[k]**2) * np.cos(0.3 * (x[i]**3 + x[j]**3 + x[k]**3))
        
        # Additional multi-modal structure with sinusoidal and exponential components
        multi_modal = 0
        for i in range(self.dim):
            multi_modal += 0.3 * np.sin(4 * x[i]) * np.cos(6 * x[i]) * np.exp(-0.04 * x[i]**2) * np.sin(0.1 * x[i]**4) * np.cos(0.2 * x[i]**3)
        
        # Enhanced non-separability with higher-dimensional coupling
        non_sep = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                non_sep += 0.1 * (x[i]**2 + x[j]**2) * np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
        
        return quadratic + chaotic + saddle + cross + interference + hyperbolic + high_order + log_perturbation + coupling + chaotic_mod + trig_interference + hyperbolic_coupling + chaotic_high_freq + cross_high_order + multi_modal + non_sep