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
        
        # Spiral Gaussian peaks with enhanced interaction
        peak_sum = 0.0
        num_peaks = min(30, self.dim * 3)
        
        for i in range(num_peaks):
            # Position peaks in spiral pattern
            angle = i * 0.7
            radius = 1.0 + i * 0.4
            peak_x = radius * np.cos(angle)
            peak_y = radius * np.sin(angle)
            
            # Adjust for dimensionality
            if self.dim >= 2:
                # Use first two dimensions for spiral placement
                dx = x[0] - peak_x
                dy = x[1] - peak_y
                distance = np.sqrt(dx**2 + dy**2)
                
                # Gaussian peak with exponential decay and interaction term
                peak_value = np.exp(-0.5 * (distance / (0.4 + i * 0.03))**2) * np.exp(-0.04 * i)
                # Add interaction between peaks
                for j in range(i):
                    if j < num_peaks:
                        angle_j = j * 0.7
                        radius_j = 1.0 + j * 0.4
                        peak_x_j = radius_j * np.cos(angle_j)
                        peak_y_j = radius_j * np.sin(angle_j)
                        dx_j = x[0] - peak_x_j
                        dy_j = x[1] - peak_y_j
                        dist_ij = np.sqrt(dx_j**2 + dy_j**2)
                        interaction = 0.1 * np.exp(-0.5 * (dist_ij / 0.5)**2) * np.exp(-0.02 * j)
                        peak_value += interaction
                
                peak_sum += peak_value
            
            # Add additional peaks in higher dimensions
            if self.dim > 2:
                for d in range(2, min(self.dim, num_peaks)):
                    if i < self.dim:
                        dx = x[d] - (i * 0.4)
                        peak_sum += np.exp(-0.5 * (dx / (0.2 + i * 0.01))**2) * np.exp(-0.02 * i)
        
        # Enhanced multimodal component with harmonic interference and additional frequencies
        multimodal = 0.0
        for i in range(self.dim):
            freq = 1.0 + i * 0.7
            amp = 1.0 / (1.0 + i * 0.3)
            # Add more complex harmonic interference term to increase complexity
            harmonic = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) + \
                       0.3 * np.sin(2 * freq * x[i]) + \
                       0.2 * np.cos(3 * freq * x[i]) + \
                       0.1 * np.sin(4 * freq * x[i])
            multimodal += amp * harmonic
        
        # Add a secondary sinusoidal modulation based on all dimensions with higher frequency
        modulate = np.sin(0.8 * r) * np.cos(0.6 * r) + 0.3 * np.sin(1.5 * r)
        
        # Add cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all components
        result = radial_sine + peak_sum + multimodal + 0.2 * modulate + 0.1 * cross_term
        
        return result