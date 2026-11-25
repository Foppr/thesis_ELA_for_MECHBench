import numpy as np

class AsymmetricRadialCouplingFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Asymmetric radial component with modified exponents
        r = np.sqrt(np.sum(x**2))
        result = 0.3 * r**5 + 0.7 * r**3 + 0.1 * r
        
        # Frequency-modulated sinusoidal terms with asymmetric amplitudes
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)
            result += (1.0 + 0.3 * np.cos(i)) * np.sin(freq * x[i]) * np.cos(0.5 * x[i]**2)
            
        # Cross-dimensional coupling with asymmetric frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_ij = 1.5 + 0.3 * np.sin(i) * np.cos(j)
                result += 0.8 * np.sin(freq_ij * x[i] + 0.7 * x[j]) * np.cos(0.3 * x[i]**2 - 0.4 * x[j]**2)
                
        # Polynomial barrier with dimensionally adaptive exponents
        for i in range(self.dim):
            exp_factor = 1.0 + 0.2 * np.sin(i)
            result += 0.6 * (x[i]**(5 + exp_factor)) * np.exp(-abs(x[i]) / 3.0)
            
        # Asymmetric radial oscillation with exponential decay
        result += 1.5 * np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-r**2 / 10.0)
        
        # Coupling between dimensions with adaptive weights based on position
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin(x[i] + x[j])
                result += weight * np.sin(2.0 * x[i] * x[j]) * np.cos(0.8 * (x[i]**2 + x[j]**2))
                
        # Asymmetric high-frequency modulation
        for i in range(self.dim):
            result += 0.4 * np.sin(15.0 * x[i] + 3.0 * np.cos(i)) * np.cos(7.0 * x[i]**2)
            
        # Central repulsion with asymmetric scaling
        result += 0.9 * np.exp(-r**2 / 4.0) * np.sin(3.0 * r) * np.cos(r)
        
        return result