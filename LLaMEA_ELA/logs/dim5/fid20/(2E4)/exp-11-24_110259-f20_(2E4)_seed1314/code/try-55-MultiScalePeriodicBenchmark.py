import numpy as np

class MultiScalePeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency and amplitude parameters for each dimension
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.gradient_weights = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multi-scale trigonometric components with varying frequencies
        trig_components = []
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            phase = self.phase_shifts[i]
            
            # Combine multiple harmonics for complex periodic structure
            component = amp * (np.sin(freq * x_scaled[i] + phase) + 
                              0.5 * np.sin(2 * freq * x_scaled[i] + phase) +
                              0.3 * np.sin(3 * freq * x_scaled[i] + phase))
            trig_components.append(component)
        
        # Adaptive gradient field with directional bias
        gradient_field = 0.0
        for i in range(self.dim):
            grad_weight = self.gradient_weights[i]
            # Directional influence based on position and gradient weights
            gradient_field += grad_weight * x_scaled[i] * np.cos(x_scaled[i])
        
        # Multi-scale interference patterns between dimensions
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling to avoid overcomplexity
                # Interference pattern with distance-dependent strength
                dist = np.abs(x_scaled[i] - x_scaled[j])
                interference += np.sin(self.frequencies[i] * x_scaled[i] + 
                                     self.frequencies[j] * x_scaled[j]) * np.exp(-dist)
        
        # Global scaling and modulation based on position magnitude
        pos_magnitude = np.sqrt(np.sum(x_scaled**2))
        global_modulation = 1.0 + 0.5 * np.sin(pos_magnitude * 3.0)
        
        # Combine all components with dynamic weighting
        result = (np.sum(trig_components) + 
                 0.3 * gradient_field + 
                 0.2 * interference + 
                 0.1 * pos_magnitude**2) * global_modulation
        
        # Add small stochastic perturbation for robustness
        noise = 0.005 * np.random.rand()
        
        return result + noise