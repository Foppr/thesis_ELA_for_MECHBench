import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal-like energy field with recursive sinusoidal components
        fractal_field = 0.0
        for i in range(self.dim):
            fractal_field += (1.0 + 0.3 * np.sin(12.0 * x_scaled[i])) * \
                           (1.0 + 0.4 * np.cos(18.0 * x_scaled[i])) * \
                           (1.0 + 0.2 * np.sin(25.0 * x_scaled[i]))
        
        # Dynamic phase coupling with time-varying weights
        phase_coupling = 0.0
        for i in range(self.dim):
            phase_coupling += np.sin(8.0 * x_scaled[i] + 3.0 * np.cos(5.0 * x_scaled[(i+1) % self.dim])) * \
                             np.cos(6.0 * x_scaled[i] + 2.0 * np.sin(4.0 * x_scaled[(i+2) % self.dim]))
        
        # Adaptive constraint modulation with multi-dimensional penalty
        penalty = 0.0
        for i in range(self.dim):
            # Quadratic penalty for boundary violations
            if abs(x_scaled[i]) > 0.9:
                penalty += 15.0 * (abs(x_scaled[i]) - 0.9)**2
            # Cross-dimensional constraint violation
            if x_scaled[i] * x_scaled[(i+1) % self.dim] < -0.6:
                penalty += 8.0 * (x_scaled[i] * x_scaled[(i+1) % self.dim] + 0.6)**2
        
        # Chaotic gradient with recursive modulation
        chaotic_grad = 0.0
        for i in range(self.dim):
            chaotic_grad += np.sin(15.0 * x_scaled[i]) * \
                          np.cos(11.0 * x_scaled[i]) * \
                          np.sin(7.0 * x_scaled[i]) * \
                          np.cos(3.0 * x_scaled[i])
        
        # Multi-scale harmonic coupling with dynamic amplitude
        harmonic_coupling = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.6 * np.sin(20.0 * x_scaled[i]) * np.cos(15.0 * x_scaled[i])
            freq = 4.0 + 2.5 * np.sin(10.0 * x_scaled[i])
            harmonic_coupling += amp * np.sin(freq * x_scaled[i] + 0.5 * np.cos(8.0 * x_scaled[i]))
        
        # Dynamic scaling based on fractal dimensionality
        r = np.sqrt(np.sum(x_scaled**2))
        dynamic_scale = 1.0 + 0.9 * np.exp(-r**2 / 3.0) + 0.4 * np.sin(7.0 * r) + 0.3 * np.cos(12.0 * r)
        
        # Cross-dimensional fractal coupling
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 0.6 + 0.4 * np.sin(3.0 * dist)
                cross_fractal += weight * np.sin(20.0 * dist) * np.cos(15.0 * dist) * np.sin(8.0 * dist)
        
        # Combine all components with dynamic weighting
        result = (dynamic_scale * 
                 (0.5 * fractal_field + 0.3 * phase_coupling + 0.2 * chaotic_grad + 0.4 * harmonic_coupling + 0.1 * cross_fractal) + 
                 0.15 * penalty)
        
        return result