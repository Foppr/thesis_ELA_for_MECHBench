import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with time-varying parameters and cross-dimensional coupling
        chaotic = 0.0
        for i in range(self.dim):
            t = 0.1 * (i + 1) * np.sin(np.sum(x))
            chaotic += np.sin(x[i] + t) * np.cos(2 * x[i] + t) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive fractal structure with dynamic coupling and phase modulation
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling = np.sin(0.5 * (x[i] + x[i+1])) * np.cos(0.3 * (x[i] - x[i+1]))
                phase_mod = np.sin(0.2 * x[i]) * np.cos(0.1 * x[i+1])
                fractal += coupling * phase_mod * np.exp(-0.05 * (x[i]**2 + x[i+1]**2))
        
        # Multi-scale resonance peaks with frequency modulation and amplitude scaling
        resonance = 0.0
        frequencies = [0.3, 0.7, 1.2, 2.5]
        amplitudes = [1.0, 0.8, 1.2, 0.9]
        for freq, amp in zip(frequencies, amplitudes):
            for i in range(self.dim):
                peak_height = amp * (1.0 + 0.5 * np.sin(freq * x[i]))
                peak_width = 0.1 + 0.4 * np.cos(freq * x[i])
                resonance += peak_height * np.exp(-0.5 * ((x[i] - freq) / peak_width)**2)
        
        # Quantum-like potential with phase interference and harmonic coupling
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(0.2 * x[i]) + np.cos(0.3 * x[i])
            potential = 0.5 * (x[i]**2) + 0.1 * np.sin(3 * x[i]) * np.cos(phase)
            quantum += potential
        
        # Logarithmic spiral with adaptive radius and directional modulation
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            adaptive_radius = radius * (1.0 + 0.3 * np.sin(0.5 * angle))
            direction_mod = np.cos(0.4 * angle) + 0.5 * np.sin(0.6 * angle)
            spiral += adaptive_radius * direction_mod * np.sin(4 * angle + 0.7 * radius)
        
        # Boundary penalty with exponential scaling and dimensionality-dependent strength
        boundary = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 1.0)
            strength = 15.0 * (1.0 + 0.2 * np.sin(i))
            boundary += strength * np.exp(-dist_from_boundary)
        
        # Cross-dimensional interaction terms to increase solution sensitivity
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                cross_interaction += interaction * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Combined fitness function with adaptive weights
        return (0.3 * chaotic + 
                0.25 * fractal + 
                0.2 * resonance + 
                0.15 * quantum + 
                0.08 * spiral + 
                0.02 * boundary +
                0.08 * cross_interaction)