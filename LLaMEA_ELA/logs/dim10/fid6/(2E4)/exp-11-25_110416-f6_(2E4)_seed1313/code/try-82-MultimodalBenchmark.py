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
            freq = 3 ** (i % 6 + 1)
            decay = np.exp(-0.18 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 5 + (i % 3)
            result += 0.38 * (x[i] - 1.3)**power + 0.32 * (x[i] + 1.8)**(power + 1)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.13 * np.exp(-0.5 * ((x[i] - 1.7) / 0.3)**2) * np.sin(30 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] - x[j]))
                result += 0.09 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.12 * np.sum(np.sin(33 * x) * np.cos(17 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.12 * np.sin(17 * x[i]) * np.exp(-0.32 * (x[i] - 1.1)**2)
            result += asym_term
            
        # Add new asymmetric sine-cosine coupling term between dimensions with modified parameters
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = np.sin(21 * x[i]) * np.cos(15 * x[j]) * (x[i] + x[j])**2
                result += 0.04 * coupling
                
        # Add additional irregularity with modified exponential decay and sine terms
        for i in range(self.dim):
            result += 0.09 * np.sin(27 * x[i]) * np.exp(-0.36 * (x[i] + 1.4)**2)
            
        # Add a new multi-modal component with increased complexity
        for i in range(self.dim):
            result += 0.11 * np.sin(39 * x[i]) * np.cos(11 * x[i]) * np.exp(-0.09 * (x[i] - 0.4)**2)
            
        return result