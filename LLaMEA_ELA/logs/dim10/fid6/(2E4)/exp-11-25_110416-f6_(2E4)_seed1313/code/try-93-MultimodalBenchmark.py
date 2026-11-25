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
            freq = 5 ** (i % 8 + 1)
            decay = np.exp(-0.3 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 7 + (i % 5)
            result += 0.5 * (x[i] - 1.3)**power + 0.4 * (x[i] + 2.1)**(power + 1)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.5 * ((x[i] - 1.9) / 0.4)**2) * np.sin(40 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.7 * (x[i] - x[j]))
                result += 0.12 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.15 * np.sum(np.sin(43 * x) * np.cos(23 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.15 * np.sin(23 * x[i]) * np.exp(-0.4 * (x[i] - 1.3)**2)
            result += asym_term
            
        # Add new asymmetric sine-cosine coupling term between dimensions with modified parameters
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                coupling = np.sin(29 * x[i]) * np.cos(21 * x[j]) * (x[i] + x[j])**2
                result += 0.05 * coupling
                
        # Add additional irregularity with modified exponential decay and sine terms
        for i in range(self.dim):
            result += 0.11 * np.sin(33 * x[i]) * np.exp(-0.45 * (x[i] + 1.6)**2)
            
        # Add a new multi-modal component with increased complexity
        for i in range(self.dim):
            result += 0.13 * np.sin(47 * x[i]) * np.cos(17 * x[i]) * np.exp(-0.12 * (x[i] - 0.6)**2)
            
        # Add ultra-high frequency chaotic modulation
        for i in range(self.dim):
            result += 0.08 * np.sin(53 * x[i]) * np.cos(29 * x[i]) * np.exp(-0.05 * (x[i] - 0.3)**2)
            
        # Add enhanced conditioning through multi-scale frequency interactions
        for i in range(self.dim):
            result += 0.06 * np.sin(37 * x[i]) * np.cos(13 * x[i]) * np.exp(-0.2 * (x[i] + 0.8)**2)
            
        # Introduce a slight modification to the chaotic component for increased difficulty
        result += 0.03 * np.sum(np.sin(59 * x) * np.cos(31 * x) * np.exp(-0.1 * x**2))
        
        # Add even more complex cross-dimensional interactions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                coupling = np.sin(31 * x[i]) * np.cos(19 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.08 * coupling
                
        # Add a new high-frequency chaotic modulation component with dynamic scaling
        for i in range(self.dim):
            result += 0.17 * np.sin(67 * x[i]) * np.cos(37 * x[i]) * np.exp(-0.03 * (x[i] + 0.5)**2)
            
        # Add a new asymmetric multi-modal term with varying amplitudes and frequencies
        for i in range(self.dim):
            result += 0.14 * np.sin(53 * x[i]) * np.cos(23 * x[i]) * np.exp(-0.08 * (x[i] - 1.2)**2)
            
        # Add a complex nested sinusoidal structure with multiple modulation frequencies
        for i in range(self.dim):
            result += 0.09 * np.sin(41 * x[i]) * np.cos(31 * x[i]) * np.sin(17 * x[i]) * np.exp(-0.15 * (x[i] + 1.8)**2)
            
        # Add a new multi-scale chaotic component with recursive frequency modulation
        for i in range(self.dim):
            result += 0.11 * np.sin(71 * x[i]) * np.cos(43 * x[i]) * np.exp(-0.06 * (x[i] - 0.9)**2)
            
        return result