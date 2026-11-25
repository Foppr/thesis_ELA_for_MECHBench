import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic fractal component with increased nesting and scaling
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 20):  # Increased nesting to 19 levels for sharper features
                scale *= 0.32  # Slightly decreased scaling factor for sharper features
                nested_sum += scale * np.sin(2**(k+4) * xi + k * np.pi/5)
            fractal += nested_sum
        
        # Enhanced time-delayed feedback with stronger quantum-like phase interactions
        feedback = 0.0
        for i in range(self.dim):
            if i > 4:
                delay = x_norm[i-1] + 0.6 * x_norm[i-2] - 0.5 * x_norm[i-3] + 0.3 * x_norm[i-4] - 0.2 * x_norm[i-5]
                # Stronger quantum phase interference
                phase = np.exp(1j * (12.0 * delay + 0.8 * i))
                feedback += np.real(phase * np.exp(-0.5 * delay**2))
            else:
                feedback += np.sin(13.0 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Advanced adaptive landscape erosion with increased roughness
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.4 + 0.6 * np.sin(5.0 * x_norm[i]) + 0.5 * np.cos(4.0 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 4.0 * x_norm[i]**3 + 2.5 * x_norm[i])
        
        # Quantum-inspired interference patterns with stronger frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 6 + 5)  # Increased base frequency variation
            # Enhanced tunneling effect
            tunneling = np.exp(-0.6 * (x_norm[i] - 0.4)**2)
            interference += tunneling * np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.5)
        
        # Enhanced cross-dimensional coupling with stronger entanglement effects
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range to 6 dimensions
                dist = np.abs(x_norm[i] - x_norm[j])
                # Stronger entanglement strength
                entanglement = 0.9 + 0.1 * np.sin(0.8 * (i + j))
                strength = entanglement * np.exp(-dist**2 * (4.0 + 0.6 * (i+j)))
                cross += strength * np.sin(25.0 * dist) * np.cos(10.0 * dist)
        
        # Enhanced quantum-inspired dynamic scaling with stronger dimensionality modulation
        dynamic_scale = 1.0 + 0.9 * np.sin(self.dim * 0.6) * np.cos(np.mean(x_norm)**4)
        
        # Combined components with adjusted weights for increased challenge and ruggedness
        weight_fractal = 0.5 + 0.1 * np.sin(self.dim * 0.5)
        weight_feedback = 0.3 + 0.2 * np.cos(self.dim * 0.3)
        weight_erosion = 0.28 + 0.18 * np.tanh(self.dim * 0.2)
        weight_interference = 0.25 + 0.09 * np.sin(self.dim * 0.25)
        weight_cross = 0.22  # Increased cross-weight for enhanced challenge
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)