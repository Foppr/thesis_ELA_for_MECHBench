import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal potential with chaotic modulation and higher frequency components
        fractal_potential = 0
        for i in range(self.dim):
            freq1 = 2.0 + 1.5 * np.sin(0.3 * x[i] + self.dim * 0.1)
            freq2 = 1.0 + 0.8 * np.cos(0.4 * x[i] + self.dim * 0.2)
            amp1 = 1.0 + 0.5 * np.sin(0.6 * x[i] + 0.3 * self.dim)
            amp2 = 0.8 + 0.3 * np.cos(0.5 * x[i] + 0.4 * self.dim)
            phase1 = 0.5 * np.sin(0.6 * x[i] + 0.3 * self.dim)
            phase2 = 0.3 * np.cos(0.7 * x[i] + 0.2 * self.dim)
            fractal_potential += (amp1 * np.sin(freq1 * x[i] + phase1) + 
                                amp2 * np.cos(freq2 * x[i] + phase2)) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced dynamic coupling with more complex interaction terms
        coupling = 0
        for i in range(self.dim):
            weight1 = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.25)
            weight2 = 0.7 + 0.2 * np.cos(0.6 * x[i] + self.dim * 0.3)
            for j in range(i+1, min(i+4, self.dim)):
                coupling += (weight1 * weight2) * (x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Multi-scale oscillatory components with more complex frequency modulation
        oscillatory = 0
        for i in range(self.dim):
            freq1 = 1.0 + 0.5 * np.sin(0.2 * x[i])
            freq2 = 2.0 + 1.0 * np.cos(0.3 * x[i])
            freq3 = 3.0 + 1.5 * np.sin(0.4 * x[i])
            freq4 = 4.0 + 2.0 * np.cos(0.5 * x[i])
            oscillatory += (np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2) * 
                          np.sin(freq3 * x[i]**3) * np.cos(freq4 * x[i]))
        
        # Enhanced adaptive conditioning with more chaotic scaling
        condition = 1.5 + 0.8 * np.sin(self.dim * 0.3 + 0.4 * np.cos(x[0] if self.dim > 0 else 0))
        
        # Improved asymmetric multimodal structure with additional terms
        asymmetric = 0
        for i in range(self.dim):
            term1 = np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3.0 * x[i])
            term2 = np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(2.5 * x[i])
            term3 = np.exp(-0.3 * x[i]**2) * np.sin(4.0 * x[i]**2)
            term4 = np.exp(-0.2 * (x[i] - 1.0)**2) * np.cos(5.0 * x[i])
            term5 = np.exp(-0.4 * (x[i] + 1.0)**2) * np.sin(6.0 * x[i]**3)
            asymmetric += term1 + term2 + term3 + term4 + term5
        
        # Combine all components with optimized weights for better fitness
        return condition * (0.35 * fractal_potential + 0.2 * coupling + 
                           0.2 * oscillatory + 0.25 * asymmetric)