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
            
        # Add stronger cross-dimensional coupling with longer-range interactions and non-linear scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.8 * (x[i] - x[j]))
                result += 0.15 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.2 * np.sum(np.sin(40 * x) * np.cos(25 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.2 * np.sin(25 * x[i]) * np.exp(-0.5 * (x[i] - 1.4)**2)
            result += asym_term
            
        # Add a novel multi-modal component with irregular spacing and variable amplitude
        for i in range(self.dim):
            result += 0.1 * np.sin(60 * x[i]) * np.cos(30 * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Add a new global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.35 * np.sin(20 * x[i])**4 + 0.25 * np.cos(15 * x[i])**3
            
        # Add a novel asymmetric sine-cosine coupling term to increase solution sensitivity and landscape complexity
        for i in range(self.dim):
            result += 0.18 * np.sin(30 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.2 * (x[i] - 1.5)**2)
            
        return result