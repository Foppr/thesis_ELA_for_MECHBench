import numpy as np

class HybridChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Asymmetric periodic valleys with directional bias
        valley_term = 0.0
        for i in range(self.dim):
            # Directional bias: different behavior based on sign of dimension
            bias_factor = 1.0 + 0.3 * np.sign(x_scaled[i])
            # Periodic valley structure with asymmetric width
            valley_width = 0.5 + 0.4 * np.sin(3.0 * x_scaled[i])**2
            valley_term += bias_factor * np.exp(-0.5 * ((x_scaled[i] % (np.pi/2)) / valley_width)**2)
        
        # Chaotic modulation with fractal-like scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic oscillations
            chaotic_freq = 10.0 + 5.0 * np.sin(2.0 * x_scaled[i])
            chaotic_term += np.sin(chaotic_freq * x_scaled[i]) * np.cos(chaotic_freq * x_scaled[i] * 0.7)
        
        # Scale-dependent ruggedness with multi-modal structure
        ruggedness_term = 0.0
        for i in range(self.dim):
            # Multiple Gaussian peaks with varying heights and widths
            peak_heights = [1.5, 2.0, 1.0, 2.5]
            peak_widths = [0.3, 0.4, 0.2, 0.5]
            peak_positions = [-1.0, -0.3, 0.5, 1.2]
            
            for h, w, p in zip(peak_heights, peak_widths, peak_positions):
                ruggedness_term += h * np.exp(-0.5 * ((x_scaled[i] - p) / w)**2)
        
        # Cross-dimensional coupling with asymmetric interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric coupling strength based on dimension indices
                asym_factor = 1.0 + 0.5 * np.sin(0.5 * (i - j))
                coupling_strength = 0.8 + 0.2 * np.cos(3.0 * (x_scaled[i] + x_scaled[j]))
                coupling_term += asym_factor * coupling_strength * np.sin(5.0 * (x_scaled[i] - x_scaled[j]))
        
        # Combined landscape with varying weights
        result = (0.3 * valley_term + 
                 0.4 * chaotic_term + 
                 0.2 * ruggedness_term + 
                 0.1 * coupling_term)
        
        return result