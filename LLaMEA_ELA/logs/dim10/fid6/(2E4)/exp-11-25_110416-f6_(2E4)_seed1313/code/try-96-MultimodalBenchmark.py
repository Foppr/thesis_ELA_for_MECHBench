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
            freq = 7 ** (i % 6 + 1)
            decay = np.exp(-0.25 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.35)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 8 + (i % 4)
            result += 0.6 * (x[i] - 1.2)**power + 0.5 * (x[i] + 2.0)**(power + 1)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.25 * np.exp(-0.5 * ((x[i] - 1.8) / 0.35)**2) * np.sin(45 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.6 * (x[i] - x[j]))
                result += 0.15 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.2 * np.sum(np.sin(47 * x) * np.cos(27 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.18 * np.sin(27 * x[i]) * np.exp(-0.35 * (x[i] - 1.4)**2)
            result += asym_term
            
        # Add new asymmetric sine-cosine coupling term between dimensions with modified parameters
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling = np.sin(31 * x[i]) * np.cos(23 * x[j]) * (x[i] + x[j])**2
                result += 0.06 * coupling
                
        # Add additional irregularity with modified exponential decay and sine terms
        for i in range(self.dim):
            result += 0.13 * np.sin(37 * x[i]) * np.exp(-0.4 * (x[i] + 1.5)**2)
            
        # Add a new multi-modal component with increased complexity
        for i in range(self.dim):
            result += 0.15 * np.sin(51 * x[i]) * np.cos(19 * x[i]) * np.exp(-0.15 * (x[i] - 0.5)**2)
            
        # Add ultra-high frequency chaotic modulation
        for i in range(self.dim):
            result += 0.09 * np.sin(57 * x[i]) * np.cos(31 * x[i]) * np.exp(-0.06 * (x[i] - 0.2)**2)
            
        # Add enhanced conditioning through multi-scale frequency interactions
        for i in range(self.dim):
            result += 0.07 * np.sin(41 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.22 * (x[i] + 0.7)**2)
            
        # Introduce a slight modification to the chaotic component for increased difficulty
        result += 0.04 * np.sum(np.sin(61 * x) * np.cos(33 * x) * np.exp(-0.12 * x**2))
        
        # Add new irregularity with asymmetric sine-cosine patterns and enhanced conditioning
        for i in range(self.dim):
            result += 0.11 * np.sin(53 * x[i]) * np.cos(29 * x[i]) * np.exp(-0.18 * (x[i] + 0.9)**2)
            
        # Add a novel asymmetric coupling term with exponential weighting
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(37 * x[i]) * np.cos(29 * x[j]) * np.exp(-0.25 * (x[i] - x[j])**2)
                result += 0.08 * coupling
                
        # Add a novel high-frequency chaotic component with modified amplitude
        result += 0.17 * np.sum(np.sin(67 * x) * np.cos(37 * x) * np.exp(-0.15 * x**2))
        
        return result