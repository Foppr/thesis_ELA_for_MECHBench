import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components with varying frequencies and higher chaos
        for i in range(self.dim):
            freq = 7 ** (i % 9 + 1)
            decay = np.exp(-0.4 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 8 + (i % 6)
            result += 0.6 * (x[i] - 1.4)**power + 0.5 * (x[i] + 2.2)**(power + 1)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.25 * np.exp(-0.5 * ((x[i] - 2.0) / 0.35)**2) * np.sin(45 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+9, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.8 * (x[i] - x[j]))
                result += 0.15 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.2 * np.sum(np.sin(47 * x) * np.cos(27 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.2 * np.sin(27 * x[i]) * np.exp(-0.5 * (x[i] - 1.4)**2)
            result += asym_term
            
        # Add new asymmetric sine-cosine coupling term between dimensions with modified parameters
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                coupling = np.sin(31 * x[i]) * np.cos(25 * x[j]) * (x[i] + x[j])**2.5
                result += 0.06 * coupling
                
        # Add additional irregularity with modified exponential decay and sine terms
        for i in range(self.dim):
            result += 0.13 * np.sin(37 * x[i]) * np.exp(-0.5 * (x[i] + 1.7)**2)
            
        # Add a new multi-modal component with increased complexity
        for i in range(self.dim):
            result += 0.15 * np.sin(51 * x[i]) * np.cos(19 * x[i]) * np.exp(-0.15 * (x[i] - 0.7)**2)
            
        # Add ultra-high frequency chaotic modulation
        for i in range(self.dim):
            result += 0.09 * np.sin(59 * x[i]) * np.cos(31 * x[i]) * np.exp(-0.06 * (x[i] - 0.4)**2)
            
        # Add enhanced conditioning through multi-scale frequency interactions
        for i in range(self.dim):
            result += 0.07 * np.sin(41 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.25 * (x[i] + 0.9)**2)
            
        # Add a new nested exponential-sine structure with ultra-high frequency components
        for i in range(self.dim):
            result += 0.18 * np.sin(61 * x[i]) * np.cos(37 * x[i]) * np.exp(-0.1 * (x[i] - 0.5)**2) * np.sin(100 * x[i])
            
        # Add a complex interaction term between all dimensions with high-order polynomial scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * (x[i]**3 + x[j]**3) * np.sin(29 * (x[i] - x[j])) * np.cos(23 * (x[i] + x[j]))
                
        return result