import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic scaling factor based on dimensionality
        self.scaling_factor = 1.0 + 0.5 * np.log10(dim + 1)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with time-varying parameters and stochastic noise
        chaotic = 0.0
        for i in range(self.dim):
            t = 0.1 * (i + 1) * np.sin(np.sum(x))
            # Add stochastic noise to increase sensitivity
            noise = np.random.normal(0, 0.05)
            chaotic += (np.sin(x[i] + t) * np.cos(2 * x[i] + t) * np.exp(-0.1 * x[i]**2) + noise)
        
        # Adaptive fractal structure with dynamic coupling and dimensionality scaling
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling = np.sin(0.5 * (x[i] + x[i+1])) * np.cos(0.3 * (x[i] - x[i+1]))
                # Apply dynamic scaling factor
                fractal += coupling * np.exp(-0.05 * (x[i]**2 + x[i+1]**2)) * self.scaling_factor
        
        # Multi-scale resonance peaks with frequency modulation and stochastic perturbations
        resonance = 0.0
        frequencies = [0.5, 1.0, 2.0, 4.0]
        for freq in frequencies:
            for i in range(self.dim):
                peak_height = 1.0 + 0.5 * np.sin(freq * x[i])
                peak_width = 0.1 + 0.3 * np.cos(freq * x[i])
                # Add stochastic perturbation to width
                width_noise = np.random.normal(0, 0.02)
                resonance += peak_height * np.exp(-0.5 * ((x[i] - freq) / (peak_width + width_noise))**2)
        
        # Quantum-like potential with phase interference and dynamic scaling
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(0.2 * x[i]) + np.cos(0.3 * x[i])
            potential = 0.5 * (x[i]**2) + 0.1 * np.sin(3 * x[i]) * np.cos(phase)
            # Apply dimensionality scaling
            quantum += potential * self.scaling_factor
        
        # Logarithmic spiral with adaptive radius and stochastic modulation
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            adaptive_radius = radius * (1.0 + 0.3 * np.sin(0.5 * angle))
            # Add stochastic modulation to radius
            radius_noise = np.random.normal(0, 0.03)
            spiral += (adaptive_radius + radius_noise) * np.sin(4 * angle + 0.7 * (radius + radius_noise))
        
        # Boundary penalty with exponential scaling and stochastic adjustment
        boundary = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 1.0)
            # Add stochastic adjustment to boundary penalty
            penalty_noise = np.random.normal(0, 0.1)
            boundary += 10.0 * np.exp(-dist_from_boundary) + penalty_noise
        
        # Combined fitness function with adaptive weights and dynamic scaling
        total = (0.3 * chaotic + 
                0.25 * fractal + 
                0.2 * resonance + 
                0.15 * quantum + 
                0.08 * spiral + 
                0.02 * boundary)
        
        # Apply final dynamic scaling based on dimensionality
        return total * self.scaling_factor