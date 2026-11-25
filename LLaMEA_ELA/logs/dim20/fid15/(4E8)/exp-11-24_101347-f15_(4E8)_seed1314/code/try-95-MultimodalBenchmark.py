import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Intensified chaotic oscillations with multiple frequency bands
        chaotic_osc = 0.0
        for i in range(self.dim):
            chaotic_osc += (np.sin(15.0 * x_scaled[i]) * np.cos(12.0 * x_scaled[i]) * 
                           np.sin(8.0 * x_scaled[i]) * np.cos(5.0 * x_scaled[i]))
        
        # Augmented radial decay with logarithmic spiral components
        r = np.sqrt(np.sum(x_scaled**2))
        radial_decay = 1.0 + 0.5 * np.exp(-r**2 / 0.5) + 0.3 * np.log(r + 1.0) + 0.2 * np.sin(10.0 * r)
        
        # Modified trigonometric coupling with phase shifts and amplitude modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(3.0 * x_scaled[i])
            amp_mod = 1.0 + 0.4 * np.cos(7.0 * x_scaled[i])
            trig_coupling += amp_mod * np.sin(6.0 * x_scaled[i] + phase_shift) * np.cos(4.0 * x_scaled[i])
        
        # Enhanced noise modulation with dynamic frequency components
        noise_mod = 0.0
        for i in range(self.dim):
            noise_mod += (0.3 * np.sin(25.0 * x_scaled[i]) + 
                         0.2 * np.cos(18.0 * x_scaled[i]) + 
                         0.1 * np.sin(30.0 * x_scaled[i]))
        
        # Complex penalty mechanism with multiple constraint types and adaptive thresholds
        penalty = 0.0
        for i in range(self.dim):
            # Distance-based penalty
            if abs(x_scaled[i]) > 0.7:
                penalty += 15.0 * (abs(x_scaled[i]) - 0.7)**3
            # Cross-dimensional interaction penalty
            if x_scaled[i] * x_scaled[(i+1) % self.dim] < -0.4:
                penalty += 8.0 * (x_scaled[i] * x_scaled[(i+1) % self.dim] + 0.4)**3
            # High-order interaction penalty
            if abs(x_scaled[i]) > 0.6 and abs(x_scaled[(i+2) % self.dim]) > 0.6:
                penalty += 5.0 * (abs(x_scaled[i]) - 0.6) * (abs(x_scaled[(i+2) % self.dim]) - 0.6)
        
        # Multi-modal structure with fractal-like frequency variations
        modal_structure = 0.0
        for i in range(self.dim):
            freq_var = 1.0 + 0.8 * np.sin(15.0 * x_scaled[i])
            amp_var = 1.0 + 0.6 * np.cos(12.0 * x_scaled[i])
            modal_structure += amp_var * np.sin(freq_var * x_scaled[i] + 
                                               1.5 * np.cos(6.0 * x_scaled[i]) + 
                                               0.8 * np.sin(9.0 * x_scaled[i]))
        
        # Cross-dimensional coupling with dynamic weights and higher-order interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 0.6 + 0.4 * np.sin(3.0 * dist)
                cross_coupling += weight * (np.sin(20.0 * dist) * np.cos(15.0 * dist) + 
                                          0.5 * np.sin(25.0 * dist))
        
        # Combine all components with refined weighting scheme
        result = (radial_decay * 
                 (0.7 * chaotic_osc + 0.2 * trig_coupling + 0.3 * modal_structure + 0.1 * cross_coupling) + 
                 0.15 * noise_mod + 0.05 * penalty)
        
        return result