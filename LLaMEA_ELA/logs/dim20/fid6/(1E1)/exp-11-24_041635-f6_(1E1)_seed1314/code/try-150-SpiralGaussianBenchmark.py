import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        log_spiral = np.sin(2.0 * r) * np.cos(0.5 * r) * np.exp(-0.15 * r)
        
        # Chaotic radial modulation with multiple frequencies
        chaotic_mod = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = 2.0 ** i
            chaotic_mod += np.sin(freq * r) * np.cos(freq * r * 0.3) * np.exp(-0.05 * i)
        
        # Spiral Gaussian peaks with varying amplitudes and widths
        peak_sum = 0.0
        num_peaks = min(25, self.dim * 3)
        
        for i in range(num_peaks):
            # Logarithmic spiral placement with random phase shifts
            angle = i * 0.3 + np.sin(i * 0.7) * 0.5
            radius = 0.5 + i * 0.2 + np.cos(i * 0.4) * 0.3
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with varying width and amplitude
                width = 0.3 + i * 0.03 + np.sin(i * 0.5) * 0.1
                amplitude = 1.0 / (1.0 + i * 0.15 + np.cos(i * 0.3) * 0.2)
                peak_value = amplitude * np.exp(-0.5 * (distance / width)**2) * np.exp(-0.08 * i)
                peak_sum += peak_value
            
            # Additional cross-dimensional coupling peaks
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.2 + np.sin(i * 0.6) * 0.1)
                        width = 0.2 + i * 0.02
                        peak_sum += np.exp(-0.5 * (dx / width)**2) * np.exp(-0.04 * i)
        
        # Cross-dimensional coupling component with high-order interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):
                coupling += np.sin(x[i] * x[j] * 0.5) * np.cos(x[i] + x[j]) * (1.0 / (1.0 + abs(x[i] - x[j]) * 0.1))
        
        # Additional chaotic multimodal component
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.8 + np.sin(i * 0.3) * 0.5
            amp = 1.0 / (1.0 + i * 0.3 + np.cos(i * 0.4) * 0.2)
            multimodal += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.sin(freq * x[i] * 0.3)
        
        # Combine all components with varying weights
        result = log_spiral + chaotic_mod + peak_sum + coupling + multimodal
        
        return result