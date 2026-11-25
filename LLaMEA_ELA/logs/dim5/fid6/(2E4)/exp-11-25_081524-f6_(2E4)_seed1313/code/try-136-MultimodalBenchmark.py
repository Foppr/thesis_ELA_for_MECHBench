import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave component with multiple logistic maps and cross-dimension coupling
        chaotic_term = 0.0
        r_values = [3.8, 3.9, 4.0, 3.7, 3.6]
        for i in range(min(5, self.dim)):
            logistic = r_values[i % len(r_values)] * x[i] * (1 - x[i] / 5.0)
            chaotic_term += np.sin(2.0 * np.pi * logistic) * np.cos(3.0 * x[i]) * np.sin(1.5 * x[(i+1) % self.dim])
        
        # Multi-peak Gaussian with dynamically adjusted positions, variances, and amplitudes
        gaussian_term = 0.0
        num_peaks = min(7, self.dim)
        for i in range(num_peaks):
            center = -4.5 + 3.0 * (i / (num_peaks - 1) if num_peaks > 1 else 0)
            variance = 0.3 + 0.7 * np.sin(0.3 * i + self.dim * 0.1)
            amplitude = 1.0 + 0.5 * np.cos(0.4 * i)
            gaussian_term += amplitude * np.exp(-0.5 * ((x[i] - center) ** 2) / variance)
        
        # Rugged saddle point structure with enhanced fractal behavior and multiple fractional Brownian motion components
        rugged_term = 0.0
        for i in range(self.dim-2):
            diff1 = x[i] - x[i+1]
            diff2 = x[i+1] - x[i+2]
            rugged_term += (diff1**3 + 0.2 * np.sin(8.0 * diff1) + diff2**2 * np.cos(0.5 * diff2)) * np.exp(-0.1 * np.abs(diff1))
        
        # Novel dynamic coupling with time-delayed interactions, multiple FBMs, and polynomial modulation
        delay_coupling = 0.0
        for i in range(self.dim-4):
            fbm1 = np.sin(0.5 * x[i]) * np.cos(0.8 * x[i+1])
            fbm2 = np.cos(0.4 * x[i+2]) * np.sin(0.6 * x[i+3])
            fbm3 = np.sin(0.7 * x[i+1]) * np.cos(0.3 * x[i+2])
            delay_coupling += (x[i] * x[i+1] + 0.3 * x[i+2] + 0.2 * x[i+3] + 
                              fbm1 + fbm2 + fbm3) * np.cos(0.4 * x[i]) * np.sin(0.2 * x[i+1])
        
        # Global scaling with enhanced sinusoidal modulation and dimensionality-dependent noise
        scale_factor = 2.0 + 0.8 * np.sin(0.3 * self.dim)
        noise = np.random.normal(0, 0.02) if self.dim > 10 else np.random.normal(0, 0.01)
        
        # Add higher-order polynomial interactions and cross-dimension coupling
        poly_interaction = 0.0
        for i in range(self.dim):
            poly_interaction += (x[i]**5 + 0.4 * x[i]**4 - 0.2 * x[i]**3 + 0.1 * x[i]**2)
        
        # Introduce a new component with trigonometric polynomial interactions and enhanced coupling
        trig_poly = 0.0
        for i in range(self.dim-1):
            trig_poly += (np.sin(x[i]) * np.cos(x[i+1]) + 
                         np.cos(2*x[i]) * np.sin(2*x[i+1]) + 
                         np.sin(3*x[i]) * np.cos(3*x[i+1]))
        
        # Combine all components with new weights to significantly increase complexity
        return (chaotic_term * 0.9 + gaussian_term * 1.1 + rugged_term * 0.8 + 
                delay_coupling * 0.7 + poly_interaction * 0.5 + trig_poly * 0.6) * scale_factor + noise