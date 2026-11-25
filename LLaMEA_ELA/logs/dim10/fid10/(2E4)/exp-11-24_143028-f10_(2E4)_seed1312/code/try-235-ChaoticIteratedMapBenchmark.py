import numpy as np

class ChaoticIteratedMapBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.memory_weights = np.random.uniform(0.1, 0.5, dim)
        self.time_varying_params = np.random.uniform(-0.5, 0.5, dim)
        # Add stochastic perturbation components
        self.stochastic_amplitudes = np.random.uniform(0.1, 0.3, dim)
        self.fractal_scales = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic iterated map component (Logistic map with memory)
        chaotic_term = 0.0
        for i in range(self.dim):
            # Memory effect: previous value influences current
            if i == 0:
                prev_x = x[-1] if self.dim > 1 else x[i]
            else:
                prev_x = x[i-1]
            
            # Time-varying parameter with stochastic component
            r = self.r_values[i] + self.time_varying_params[i] * np.sin(0.1 * sum(x)) + \
                self.stochastic_amplitudes[i] * np.random.uniform(-1, 1)
            
            # Logistic map with memory effect and fractal scaling
            x_new = r * x[i] * (1 - x[i]) + self.memory_weights[i] * (x[i] - prev_x)
            chaotic_term += self.fractal_scales[i] * x_new**2
            
        # Cross-dimensional coupling with enhanced nonlinearity
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced phase-modulated interaction with stochastic perturbation
                phase = np.sin(0.3 * (x[i] + x[j])) + 0.1 * np.random.uniform(-1, 1)
                coupling_term += np.sin(x[i] * x[j]) * np.cos(phase) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Time-varying attractor component with adaptive scaling
        attractor_term = 0.0
        for i in range(self.dim):
            # Dynamic attractor center that changes with time and fractal scaling
            t = sum(x) / self.dim
            center = np.sin(0.2 * t + i) * 2.0 * self.fractal_scales[i]
            attractor_term += (x[i] - center)**4
            
        # Multi-scale periodic modulation with stochastic perturbations
        periodic_term = 0.0
        for i in range(self.dim):
            # Multiple frequency components with fractal scaling
            freqs = [1.0, 2.0, 3.0, 5.0]
            for f in freqs:
                periodic_term += np.sin(f * x[i] + np.cos(f * 0.5)) * np.exp(-0.05 * x[i]**2) * self.fractal_scales[i]
                
        # Boundary penalty with enhanced fractal-like scaling and stochastic component
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_to_boundary = min(abs(x[i] + 5.0), abs(x[i] - 5.0))
            if dist_to_boundary < 0.5:
                boundary_penalty += (10.0 * np.exp(-dist_to_boundary**2) + 2.0 * np.sin(20 * x[i])) * self.fractal_scales[i]
                
        # Add stochastic noise component to increase problem difficulty
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += np.random.uniform(-0.5, 0.5) * np.sin(0.1 * x[i])
            
        # Combine all components with adaptive weights and add noise
        result = 0.7 * chaotic_term + 0.5 * coupling_term + 0.6 * attractor_term + \
                 0.4 * periodic_term + 0.3 * boundary_penalty + 0.1 * noise_component
        
        return result