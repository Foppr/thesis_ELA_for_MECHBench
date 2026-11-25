import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic component with improved parameter tuning
        chaotic = 0.0
        for i in range(self.dim):
            t = 0.15 * (i + 1) * np.sin(np.sum(x) * 0.7)
            chaotic += np.sin(x[i] + t) * np.cos(2.5 * x[i] + t) * np.exp(-0.12 * x[i]**2)
        
        # Modified adaptive fractal structure with stronger coupling
        fractal = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling = np.sin(0.7 * (x[i] + x[i+1])) * np.cos(0.4 * (x[i] - x[i+1]))
                fractal += coupling * np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
        
        # Adjusted multi-scale resonance peaks with modified frequency and amplitude
        resonance = 0.0
        frequencies = [0.4, 0.8, 1.6, 3.2]
        for freq in frequencies:
            for i in range(self.dim):
                peak_height = 1.2 + 0.6 * np.sin(freq * x[i])
                peak_width = 0.08 + 0.25 * np.cos(freq * x[i])
                resonance += peak_height * np.exp(-0.5 * ((x[i] - freq) / peak_width)**2)
        
        # Refined quantum-like potential with enhanced interference terms
        quantum = 0.0
        for i in range(self.dim):
            phase = np.sin(0.25 * x[i]) + np.cos(0.35 * x[i])
            potential = 0.6 * (x[i]**2) + 0.15 * np.sin(3.5 * x[i]) * np.cos(phase)
            quantum += potential
        
        # Modified logarithmic spiral with dynamic radius scaling
        spiral = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x[i], x[(i+1) % self.dim])
            radius = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            adaptive_radius = radius * (1.0 + 0.4 * np.sin(0.6 * angle))
            spiral += adaptive_radius * np.sin(5 * angle + 0.8 * radius)
        
        # Improved boundary penalty with sharper scaling
        boundary = 0.0
        for i in range(self.dim):
            dist_from_boundary = min(5.0 - np.abs(x[i]), 1.2)
            boundary += 12.0 * np.exp(-dist_from_boundary * 1.5)
        
        # Combined fitness function with optimized weights
        return (0.35 * chaotic + 
                0.28 * fractal + 
                0.18 * resonance + 
                0.12 * quantum + 
                0.05 * spiral + 
                0.02 * boundary)