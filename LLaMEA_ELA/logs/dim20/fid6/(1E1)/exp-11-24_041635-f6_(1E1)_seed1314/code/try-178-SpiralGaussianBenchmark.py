import numpy as np

class SpiralGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial chaotic component
        r = np.sqrt(np.sum(x**2))
        radial_chaos = np.sin(5.0 * r) * np.cos(3.0 * r) * np.exp(-0.15 * r)
        
        # Logarithmic spiral Gaussian peaks
        peak_sum = 0.0
        num_peaks = min(30, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in logarithmic spiral pattern
            angle = i * 0.3 + np.sin(i * 0.1) * 0.5
            radius = np.exp(i * 0.2) * 0.5
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with exponential decay and dynamic variance
                variance = 0.3 + i * 0.03 + 0.1 * np.sin(i * 0.7)
                peak_value = np.exp(-0.5 * (distance / variance)**2) * np.exp(-0.08 * i)
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.4 + np.cos(i * 0.3) * 0.2)
                        variance = 0.2 + i * 0.02 + 0.05 * np.sin(i * 0.5)
                        peak_sum += np.exp(-0.5 * (dx / variance)**2) * np.exp(-0.04 * i)
        
        # Enhanced multimodal component with multiple harmonic interference
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.7 + 0.3 * np.sin(i * 0.5)
            amp = 1.0 / (1.0 + i * 0.3 + 0.2 * np.cos(i * 0.4))
            # Add multiple harmonic interference terms to increase complexity
            harmonic = (np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + 
                       0.5 * np.sin(2 * freq * x[i]) * np.cos(1.5 * freq * x[i]) +
                       0.3 * np.sin(3 * freq * x[i]))
            multimodal += amp * harmonic
        
        # Dynamic noise modulation based on all dimensions
        noise_mod = 0.0
        for i in range(self.dim):
            noise_mod += np.sin(x[i] * (2.0 + 0.1 * i)) * np.cos(x[i] * (1.5 + 0.05 * i))
        
        # Add a secondary chaotic modulation based on all dimensions
        modulate = np.sin(0.3 * r) * np.cos(0.4 * r) * np.sin(0.2 * r)
        
        # Combine all components
        result = radial_chaos + peak_sum + multimodal + 0.3 * noise_mod + 0.15 * modulate
        
        return result