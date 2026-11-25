import numpy as np

class OscillatoryAdaptiveBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.sin_phase = np.random.uniform(0.0, 2*np.pi, size=dim)
        
        # Parabolic basin parameters with adaptive scaling
        self.basin_centers = np.random.uniform(-4.0, 4.0, size=dim)
        self.basin_widths = np.random.uniform(0.5, 3.0, size=dim)
        self.basin_depths = np.random.uniform(1.0, 5.0, size=dim)
        
        # Dynamic gradient fields with time-varying components
        self.gradient_magnitude = np.random.uniform(0.5, 2.0, size=dim)
        self.gradient_directions = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        
        # Time-dependent oscillation parameters for dynamic landscape
        self.time_freq = np.random.uniform(0.1, 0.5, size=dim)
        self.time_amp = np.random.uniform(0.1, 1.0, size=dim)
        
        # Cross-dimensional coupling with modified weights (increased chaos)
        self.coupling_weights = np.random.uniform(0.5, 2.5, size=(dim, dim))
        
        # Multi-scale harmonic components with altered amplitudes
        self.harmonic_freqs = np.random.uniform(2.0, 10.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.5, 2.0, size=dim)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.05, 0.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 3.0, size=dim)
        
        # Basin interaction terms with varying influence ranges
        self.basin_influence = np.random.uniform(0.5, 2.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component
        sin_component = 0.0
        for i in range(self.dim):
            sin_val = self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.sin_phase[i])
            sin_component += sin_val
            
        # Parabolic basin component with adaptive scaling
        basin_component = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            # Adaptive width based on distance from center
            adaptive_width = self.basin_widths[i] * (1.0 + 0.5 * np.sin(dist))
            basin_val = self.basin_depths[i] * (dist / adaptive_width) ** 2
            basin_component += basin_val
            
        # Gradient field component with dynamic direction
        grad_component = 0.0
        for i in range(self.dim):
            grad_val = 0.0
            for j in range(self.dim):
                grad_val += self.gradient_directions[i, j] * (x[j] - self.basin_centers[j])
            grad_component += self.gradient_magnitude[i] * grad_val
            
        # Time-varying oscillation component
        time_component = 0.0
        for i in range(self.dim):
            time_val = self.time_amp[i] * np.sin(self.time_freq[i] * x[i])
            time_component += time_val
            
        # Cross-dimensional coupling with modified weights (increased chaos)
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_weights[i, j] * x[i] * x[j]
                    
        # Multi-scale harmonic component with adjusted amplitudes
        harmonic_component = 0.0
        for i in range(self.dim):
            harmonic_val = self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * x[i])
            harmonic_component += harmonic_val
            
        # Noise component with varying intensities
        noise_component = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_component += noise_val
            
        # Basin interaction terms with distance-dependent influence
        basin_interaction = 0.0
        for i in range(self.dim):
            dist = np.abs(x[i] - self.basin_centers[i])
            influence = self.basin_influence[i] / (1.0 + dist)
            basin_interaction += influence
            
        # Combine all components with modified weights to increase complexity
        return (2.5 * sin_component + 
                1.8 * basin_component + 
                1.6 * grad_component + 
                1.1 * time_component + 
                0.9 * coupling_component + 
                1.0 * harmonic_component + 
                0.7 * noise_component + 
                0.6 * basin_interaction)