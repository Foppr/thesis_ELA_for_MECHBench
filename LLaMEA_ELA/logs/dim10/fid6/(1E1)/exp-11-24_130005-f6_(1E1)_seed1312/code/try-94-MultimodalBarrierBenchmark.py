import numpy as np

class MultimodalBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quantum-like harmonic potential with varying frequencies
        quantum_harmonic = 0.0
        for i in range(self.dim):
            quantum_harmonic += (x_scaled[i]**2 + 0.3 * np.sin(10.0 * x_scaled[i]) + 
                               0.1 * np.cos(15.0 * x_scaled[i]))
        
        # Chaotic tent map component for irregularity
        tent_map = 0.0
        for i in range(self.dim):
            tent_val = 2.0 * np.abs(x_scaled[i] - 0.5)
            if x_scaled[i] > 0.5:
                tent_val = 1.0 - tent_val
            tent_map += tent_val
        
        # Fractal-like cross-terms with recursive structure
        fractal_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create fractal-like interaction using sine and cosine
                fractal_cross += np.sin(3.0 * x_scaled[i] * x_scaled[j]) * \
                               np.cos(2.0 * (x_scaled[i]**2 + x_scaled[j]**2)) * \
                               np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Exponential decay barriers with fractal-like positioning
        barrier_term = 0.0
        for i in range(self.dim):
            # Create multiple barrier peaks using chaotic positioning
            barrier_positions = [np.sin(i) * 0.5, np.cos(i) * 0.3, -np.sin(i) * 0.4]
            for pos in barrier_positions:
                barrier_term += np.exp(-10.0 * (x_scaled[i] - pos)**2)
        
        # Multi-scale sinusoidal cross-terms with varying amplitudes
        multi_scale_cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.0 + 0.5 * np.sin(x_scaled[i])
                freq_j = 1.0 + 0.5 * np.cos(x_scaled[j])
                multi_scale_cross += np.sin(freq_i * x_scaled[i] + freq_j * x_scaled[j]) * \
                                   np.cos(freq_i * x_scaled[i] - freq_j * x_scaled[j]) * \
                                   (1.0 + 0.2 * np.sin(5.0 * x_scaled[i]))
        
        # Radial fractal component with multiple scales
        r = np.sqrt(np.sum(x_scaled**2))
        radial_fractal = np.exp(-r**2) * (1.0 + 0.3 * np.sin(10.0 * r) + 
                                         0.2 * np.cos(15.0 * r))
        
        # Combined landscape with increased complexity
        return 2.0 * quantum_harmonic + 1.2 * tent_map + 0.8 * fractal_cross + \
               1.0 * barrier_term + 0.9 * multi_scale_cross + 0.7 * radial_fractal + 3.0