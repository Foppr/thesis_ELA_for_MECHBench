import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial sinusoidal component
        r = np.sqrt(np.sum(x**2))
        radial_sine = np.sin(3.0 * r) * np.exp(-0.1 * r)
        
        # Spiral Gaussian peaks with chaotic modulation
        peak_sum = 0.0
        num_peaks = min(25, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in spiral pattern with tent map chaos
            angle = i * 0.5 + 0.1 * np.sin(i * 1.3)
            radius = 1.0 + i * 0.3 + 0.2 * np.cos(i * 0.7)
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Adaptive Gaussian peak width based on peak index
                adaptive_width = 0.5 + i * 0.03 + 0.1 * np.sin(i * 0.5)
                peak_value = np.exp(-0.5 * (distance / adaptive_width)**2) * np.exp(-0.05 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.3 + 0.1 * np.cos(i * 0.8))
                        adaptive_width = 0.3 + i * 0.02 + 0.05 * np.sin(i * 0.6)
                        peak_sum += np.exp(-0.5 * (dx / adaptive_width)**2) * np.exp(-0.03 * i)
        
        # Enhanced multimodal component with harmonic interference and additional chaos
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.5 + 0.1 * np.sin(i * 0.9)
            amp = 1.0 / (1.0 + i * 0.2 + 0.05 * np.cos(i * 0.4))
            # Add chaotic harmonic interference term to increase complexity
            harmonic = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + 0.3 * np.sin(2 * freq * x[i])
            # Add chaotic modulation based on dimension index
            chaotic_mod = 0.1 * np.sin(i * 2.3) * np.cos(i * 1.7)
            multimodal += amp * (harmonic + chaotic_mod)
        
        # Add a secondary sinusoidal modulation based on all dimensions with chaotic phase
        modulate = np.sin(0.5 * r + 0.2 * np.sin(r * 0.3)) * np.cos(0.3 * r + 0.1 * np.cos(r * 0.4))
        
        # Add a chaotic noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(x[i] * (i + 1) * 2.0 + 0.3 * np.cos(x[i] * 0.5))
        
        # Combine all components
        result = radial_sine + peak_sum + multimodal + 0.2 * modulate + noise
        
        return result