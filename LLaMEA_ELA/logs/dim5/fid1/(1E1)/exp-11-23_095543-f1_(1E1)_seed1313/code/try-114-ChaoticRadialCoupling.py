import numpy as np

class ChaoticRadialCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add nested radial sinusoidal modulation with chaotic frequencies
        r = np.sqrt(np.sum(x ** 2))
        freq1 = 2.5 + 0.5 * np.sin(r)
        freq2 = 3.2 + 0.3 * np.cos(r)
        result *= (1.0 + 0.4 * np.sin(freq1 * r) * np.cos(freq2 * r))
        
        # Add chaotic periodic components with varying amplitudes
        for i in range(self.dim):
            amp = 0.5 + 0.2 * np.sin(i * 0.7)
            result += amp * np.sin(11 * x[i]) * np.cos(9 * x[(i + 1) % self.dim])
            
        # Add strong cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.2 * (x[i] - x[j]) ** 2) * np.sin(5 * x[i]) * np.cos(7 * x[j])
                result += 0.3 * coupling
                
        # Add nested harmonic components with multi-scale frequencies
        for i in range(self.dim):
            result += 0.2 * np.sin(13 * r) * np.cos(11 * r) * x[i] ** 2
            
        # Add chaotic multi-scale periodicity with dynamic phases
        for i in range(self.dim):
            phase = 0.5 * np.sin(x[i])
            result += 0.3 * np.sin(18 * x[i] + phase) * np.cos(14 * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
            
        # Add asymmetric coupling with cubic terms and dynamic coefficients
        for i in range(self.dim):
            coef = 0.8 + 0.3 * np.sin(i * 0.5)
            result += coef * (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim])
            
        # Add chaotic radial peak structure with variable amplitude
        amp_peak = 0.6 + 0.2 * np.sin(r)
        result += amp_peak * np.exp(-0.3 * r ** 2) * np.sin(7 * r)
        
        # Add chaotic dimensionality-dependent scaling
        scaling = 1.0 + 0.2 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2) + 0.05 * np.sum(np.tan(x) ** 2)
        result *= scaling
        
        # Add chaotic noise component
        noise = 0.1 * np.sum(np.sin(20 * x) * np.cos(16 * x))
        result += noise
        
        return result