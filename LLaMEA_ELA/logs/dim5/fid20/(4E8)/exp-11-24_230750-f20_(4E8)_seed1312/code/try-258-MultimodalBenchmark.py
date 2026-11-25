import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with time-varying parameters and asymmetric coupling
        chaotic = 0.0
        for i in range(self.dim):
            t = 0.1 * (i + 1) * np.sin(np.sum(x))
            chaotic += np.sin(x[i] + t) * np.cos(2 * x[i] + t) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive fractal structure with dynamic coupling and time-varying strength
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling_strength = 0.5 + 0.5 * np.sin(0.2 * (i + 1) * np.sum(x))
                coupling = coupling_strength * np.sin(0.5 * (x[i] + x[i+1])) * np.cos(0.3 * (x[i] - x[i+1]))
                fractal += coupling * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
        
        # Multi-scale resonance peaks with frequency modulation and asymmetric Gaussian components
        resonance = 0.0
        frequencies = [0.5, 1.0, 2.0, 4.0]
        for freq in frequencies:
            for i in range(self.dim):
                peak_height = 1.0 + 0.5 * np.sin(freq * x[i])
                peak_width = 0.1 + 0.3 * np.cos(freq * x[i])
                # Asymmetric Gaussian component
                asymmetry = 0.2 * np.sin(0.7 * x[i])
                resonance += (peak_height + asymmetry) * np.exp(-0.5 * ((x[i] - freq) / peak_width)**2)
        
        # Quantum-like potential with phase interference and time-varying coefficients
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(0.2 * x[i]) + np.cos(0.3 * x[i])
            time_varying_coeff = 0.5 + 0.5 * np.sin(0.1 * (i + 1) * np.sum(x))
            potential = time_varying_coeff * (0.5 * (x[i]**2) + 0.1 * np.sin(3 * x[i]) * np.cos(phase))
            quantum += potential
        
        # Logarithmic spiral with adaptive radius and time-varying angle
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            time_varying_angle = angle * (1.0 + 0.2 * np.sin(0.3 * (i + 1) * np.sum(x)))
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            adaptive_radius = radius * (1.0 + 0.3 * np.sin(0.5 * time_varying_angle))
            spiral += adaptive_radius * np.sin(4 * time_varying_angle + 0.7 * radius)
        
        # Boundary penalty with exponential scaling and asymmetric behavior
        boundary = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 1.0)
            # Asymmetric penalty based on direction from boundary
            penalty_factor = 1.0 + 0.5 * np.sin(0.5 * x[i])
            boundary += 10.0 * np.exp(-dist_from_boundary) * penalty_factor
        
        # Combined fitness function with adaptive weights and time-varying coefficients
        total_weight = 0.3 + 0.2 * np.sin(0.1 * np.sum(x))
        chaotic_weight = 0.3 * (1.0 + 0.1 * np.sin(0.2 * np.sum(x)))
        fractal_weight = 0.25 * (1.0 + 0.1 * np.cos(0.2 * np.sum(x)))
        resonance_weight = 0.2 * (1.0 + 0.1 * np.sin(0.3 * np.sum(x)))
        quantum_weight = 0.15 * (1.0 + 0.1 * np.cos(0.3 * np.sum(x)))
        spiral_weight = 0.08 * (1.0 + 0.1 * np.sin(0.4 * np.sum(x)))
        boundary_weight = 0.02 * (1.0 + 0.1 * np.cos(0.4 * np.sum(x)))
        
        return (chaotic_weight * chaotic + 
                fractal_weight * fractal + 
                resonance_weight * resonance + 
                quantum_weight * quantum + 
                spiral_weight * spiral + 
                boundary_weight * boundary)