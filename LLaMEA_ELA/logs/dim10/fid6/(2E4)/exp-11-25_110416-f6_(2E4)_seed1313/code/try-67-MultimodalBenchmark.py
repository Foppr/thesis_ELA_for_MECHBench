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
            freq = 8 ** (i % 10 + 1)
            decay = np.exp(-0.3 * np.abs(x[i]))
            result += decay * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.25)
            
        # Add enhanced polynomial penalties with higher exponents and stronger coefficients
        for i in range(self.dim):
            power = 9 + (i % 7)
            result += 0.7 * (x[i] - 1.3)**power + 0.6 * (x[i] + 2.1)**(power + 1)
            
        # Add a more complex global minimum structure with multiple peaks and increased amplitude
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.5 * ((x[i] - 1.8) / 0.4)**2) * np.sin(50 * x[i])
            
        # Add stronger cross-dimensional coupling with longer-range interactions and non-linear scaling
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.9 * (x[i] - x[j]))
                result += 0.2 * interaction
                
        # Add a highly chaotic component with nested sinusoidal patterns and increased scaling
        chaotic_term = 0.25 * np.sum(np.sin(45 * x) * np.cos(30 * x))
        result += chaotic_term
        
        # Add a new layer of irregularity with asymmetric peaks and non-uniform scaling
        for i in range(self.dim):
            asym_term = 0.25 * np.sin(30 * x[i]) * np.exp(-0.6 * (x[i] - 1.3)**2)
            result += asym_term
            
        # Add a novel multi-modal component with irregular spacing and variable amplitude
        for i in range(self.dim):
            result += 0.15 * np.sin(65 * x[i]) * np.cos(35 * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Add a new global structure with multiple local minima and enhanced non-linearity
        for i in range(self.dim):
            result += 0.4 * np.sin(25 * x[i])**4 + 0.3 * np.cos(20 * x[i])**3
            
        # Add a novel asymmetric sine-cosine coupling term to increase solution sensitivity and landscape complexity
        for i in range(self.dim):
            result += 0.2 * np.sin(35 * x[i]) * np.cos(20 * x[i]) * np.exp(-0.25 * (x[i] - 1.4)**2)
            
        return result