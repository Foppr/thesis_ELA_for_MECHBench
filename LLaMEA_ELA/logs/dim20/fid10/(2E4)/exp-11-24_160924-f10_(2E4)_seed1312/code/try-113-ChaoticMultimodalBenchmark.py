import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Sinusoidal terms with chaotic modulation of frequency and amplitude
            freq_mod = 1.0 + 0.3 * np.sin(2.0 * xi) * np.cos(0.5 * xi)
            amp_mod = 1.0 + 0.4 * np.tan(0.7 * xi) * np.sin(1.3 * xi)
            result += amp_mod * np.sin(freq_mod * xi) * np.cos(0.8 * xi)
            
        # Polynomial coupling with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            # Chaotic coefficient based on dimension index and sinusoidal modulation
            coeff = 1.0 + 0.5 * np.sin(0.3 * i) * np.cos(0.4 * xi)
            result += coeff * (xi**6 - 2 * xi**4 + xi**2)
            
        # Add non-separable coupling with chaotic trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength with dynamic modulation
                coupling = 1.5 + 0.6 * np.sin(0.2 * (i + j)) * np.cos(0.3 * (i - j))
                # Coupling term with enhanced trigonometric interaction
                interaction = np.sin(xi) * np.cos(xj) + 0.4 * np.tan(xi * xj)
                result += coupling * interaction * np.exp(-0.1 * (xi**2 + xj**2))
                
        # Add chaotic gradient complexity through rational functions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                # Rational function with chaotic numerator and denominator
                num = np.sin(xi) + 0.5 * np.cos(x[i+1]) + 0.3 * np.tan(xi * x[i+1])
                den = np.cos(xi) + 0.4 * np.sin(x[i+1]) + 0.2 * np.tan(xi + x[i+1])
                # Add chaotic modulation to the rational function
                chaos_mod = 1.0 + 0.3 * np.sin(0.5 * (xi + x[i+1]))
                result += chaos_mod * (num / den)
                
        # Add chaotic penalty near global optimum to increase convergence difficulty
        result += 0.7 * np.sum(np.exp(-0.3 * (x - 0.0)**2)) + 0.4 * np.sum(np.abs(x - 0.0)**4)
        
        # Add multi-modal structure with periodic peaks
        for i in range(self.dim):
            xi = x[i]
            # Multiple periodic peaks with chaotic positioning
            peak1 = 1.0 / (1.0 + (xi - 2.0)**2 + 0.3 * np.sin(5.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 2.0)**2 + 0.2 * np.cos(4.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.0)**2 + 0.25 * np.tan(3.0 * xi))
            result += 0.5 * (peak1 + peak2 + peak3)
            
        # Add chaotic saddle points with rational polynomial modulation
        for i in range(self.dim):
            xi = x[i]
            # Saddle point inducing term with chaotic modulation
            saddle_term = (xi**4 - 2 * xi**2) / (xi**2 + 0.5 + 0.3 * np.cos(4.0 * xi))
            result += 0.3 * saddle_term
            
        return result